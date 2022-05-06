from flask import request
import pandas as pd
# setting disactivate chained_assignment WARNING from panda
pd.options.mode.chained_assignment = None

# Setup of the Google Cloud utilities
from google.cloud import bigquery
from google.oauth2 import service_account
import json, os


# Parameters


# DB connection credentials
# Google Cloud services
gcp_service_account_credentials_json_filename = 'epfl-course-f41b0ed796f9.json' #need to upload the json credential files to the root directory of the google colab files
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gcp_service_account_credentials_json_filename
credentials = service_account.Credentials.from_service_account_file(gcp_service_account_credentials_json_filename, scopes=['https://www.googleapis.com/auth/bigquery', 'https://www.googleapis.com/auth/drive'])
project_id = 'epfl-course'
bigquery_client = bigquery.Client(credentials=credentials, project=project_id)
bigquery_client = bigquery.Client()


# BQ Utilities
#Execute a query in BQ
def bq_execute_query(query, mode="INTERACTIVE", wait=False, format=None):
    job_config = bigquery.QueryJobConfig(priority="bigquery.QueryPriority.{}".format(mode)) # Run at BATCH priority, which won't count toward concurrent rate limit, otherwise INTERACTIVE.
    query_job = bigquery_client.query(query, job_config)
    if wait==True:
        print("Executed BQ query: ", query_job.result())
    if format=="df":
        return(query_job.to_dataframe())
    if format=="json":
        df = query_job.to_dataframe()
        return df.to_json(orient='records')
    else:
        return(query_job)

#Upload a DF to BQ
def upload_df_to_bq(df, bq_destination_table, write_disposition="WRITE_APPEND"):
    #bq_table_name = "epfl-course.dataset.table"
    job_config = bigquery.LoadJobConfig(create_disposition="CREATE_IF_NEEDED", 
                                        write_disposition=write_disposition)
    #source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    upload_df_to_bq_job = bigquery_client.load_table_from_dataframe(
        df, bq_destination_table, job_config = job_config)
    print("Uploaded DF to BQ: ",upload_df_to_bq_job.result()) 

#Upload a JSON to BQ
def upload_json_to_bq(json_object, bq_table):
    try:
        job_config = bigquery.LoadJobConfig()
        job_config.autodetect = False #Change to True if the table on BQ does not exits
        job_config.max_bad_records = 0
        job_config.ignore_unknown_values = True
        job_config.source_format = 'NEWLINE_DELIMITED_JSON'
        job_config.create_disposition= "CREATE_IF_NEEDED"
        job_config.write_disposition= "WRITE_APPEND"
        job = bigquery_client.load_table_from_file(json_object, bq_table, job_config = job_config)
        print("Loaded JSON to BQ table {} as job {}".format(bq_table, job.result()))
        assert job.job_type == 'load'
        assert job.state == 'DONE'
    except:
        print("ERROR Could not load JSON to BQ table {} as job {}".format(bq_table, job.result()))

# API utilities
# !! NOT IMPLEMENTED AUTHENTICATION
def internal_auth_required(f):
    # @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'internal_auth_token' in request.headers:
            token = request.headers['internal_auth_token']
        if not token:
            return 'Unauthorized Access!', 401

        auth_token = "data_viz"  # password
        if token != auth_token:
            return 'Unauthorized Access!', 401
        return f(*args, **kwargs)
    return decorated


def parse_request_headers():
    # @wraps(f)
    def process_request_headers(*args, **kwargs):
        if ('parameter1' in request.headers):
            parameter1 = request.headers.get('parameter1')
            return parameter1
        else:
            return 'No requested parameters in headers', 412
    return process_request_headers()

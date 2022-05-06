from utils import *
import pandas as pd
import json
import datetime
import flask


def get_bq_data_function(query):
    try:
        print("query to execute: ")
        print(query)
        query_result = bq_execute_query(query, format="json")
        print("query worked")
        return query_result, 200
    except:
        try:
            message = query_result
        except:
            message = "query failed"
        return {"no result in query message": str(message)}, 400

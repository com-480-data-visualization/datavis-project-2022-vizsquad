from random import random

import requests
import os
import hashlib
import csv
import json
import io
import time
import tqdm
import random

import pandas as pd

TIMEOUT_TIME = 120

def callMovebankAPI(params):
    # Requests Movebank API with ((param1, value1), (param2, value2),).
    # Assumes the environment variables 'mbus' (Movebank user name) and 'mbpw' (Movebank password).
    # Returns the API response as plain text.

    response = requests.get('https://www.movebank.org/movebank/service/direct-read', params=params,
                            auth=(os.environ['mbus'], os.environ['mbpw']), timeout=TIMEOUT_TIME)
    print("Request " + response.url)
    if response.status_code == 200:  # successful request
        if 'License Terms:' in str(response.content):
            # only the license terms are returned, hash and append them in a subsequent request.
            # See also
            # https://github.com/movebank/movebank-api-doc/blob/master/movebank-api.md#read-and-accept-license-terms-using-curl
            print("Has license terms")
            hash = hashlib.md5(response.content).hexdigest()
            params = params + (('license-md5', hash),)
            # also attach previous cookie:
            response = requests.get('https://www.movebank.org/movebank/service/direct-read', params=params,
                                    cookies=response.cookies, auth=(os.environ['mbus'], os.environ['mbpw']), timeout=TIMEOUT_TIME)
            if response.status_code == 403:  # incorrect hash
                print("Incorrect hash")
                return ''
        return response.content.decode('utf-8')
    print(str(response.content))
    return ''


def getAllDownloadableStudies():
    studies = callMovebankAPI((('entity_type', 'study'), ('i_have_download_access', 'true')))
    if len(studies) > 0:
        # parse raw text to dicts
        studies = csv.DictReader(io.StringIO(studies), delimiter=',')
        return [s for s in studies if s['i_have_download_access'] == 'true']
    return []


def getIndividualsByStudy(study_id):
    params = (('entity_type', 'individual'), ('study_id', study_id))

    deployments = callMovebankAPI(params)
    if len(deployments) > 0:
        deployments = csv.DictReader(io.StringIO(deployments), delimiter=',')
        return [d for d in deployments]
    return []


def getTagsByStudy(study_id):
    params = (('entity_type', 'tag'), ('study_id', study_id))

    tags = callMovebankAPI(params)
    if len(tags) > 0:
        tags = csv.DictReader(io.StringIO(tags), delimiter=',')
        return [t for t in tags]
    return []


def getDeploymentByStudy(study_id):
    params = (('entity_type', 'deployment'), ('study_id', study_id))

    deployments = callMovebankAPI(params)
    if len(deployments) > 0:
        deployments = csv.DictReader(io.StringIO(deployments), delimiter=',')
        return [d for d in deployments]
    return []


def getSensorsByStudy(study_id):
    params = (('entity_type', 'sensor'), ('tag_study_id', study_id))

    sensors = callMovebankAPI(params)
    if len(sensors) > 0:
        sensors = csv.DictReader(io.StringIO(sensors), delimiter=',')
        return [s for s in sensors]
    return []


def getAllTagTypes():
    params = (('entity_type', 'tag_type'),)

    tag_types = callMovebankAPI(params)
    if len(tag_types) > 0:
        tag_types = csv.DictReader(io.StringIO(tag_types), delimiter=',')
        return [t for t in tag_types]
    return []


def getAllTaxons():
    params = (('entity_type', 'taxon'),)

    taxons = callMovebankAPI(params)
    if len(taxons) > 0:
        taxons = csv.DictReader(io.StringIO(taxons), delimiter=',')
        return [t for t in taxons]
    return []


def getEventsByStudy(study_id):
    params = (('entity_type', 'event'), ('study_id', study_id),
              ('attributes', "timestamp,location_lat,location_long,individual_id,tag_id,"
                             "manually_marked_outlier,manually_marked_valid,algorithm_marked_outlier,"
                             "individual_local_identifier,individual_taxon_canonical_name"),)

    events = callMovebankAPI(params)
    if len(events) > 0:
        events = csv.DictReader(io.StringIO(events), delimiter=',')
        return [e for e in events]
    return []


def getStudiesBySensor(studies, sensorname='GPS'):
    return [s for s in studies if sensorname in s['sensor_type_ids']]


def addStudyId(list, study_id):
    for item in list:
        item.update({'study_id': study_id})


def getStudyAttributesByStudy(study_id, sensor_type_id):
    params = (('entity_type', 'study_attribute'), ('study_id', study_id), ('sensor_type_id', sensor_type_id))

    attributes = callMovebankAPI(params)
    if len(attributes) > 0:
        attributes = csv.DictReader(io.StringIO(attributes), delimiter=',')
        return [a for a in attributes]
    return []


def getAllStudyAttributesByStudy(study_id, sensor_type_id_set):
    attributes = []
    for sensor_type_id in sensor_type_id_set:
        attributes.extend(getStudyAttributesByStudy(study_id, sensor_type_id))
    return attributes


if __name__ == "__main__":
    downloaded_studies = json.load(open('downloaded_studies.json'))

    allDownloadableStudies = getStudiesBySensor(getAllDownloadableStudies())
    print("Number of studies:", len(allDownloadableStudies))

    studies = pd.DataFrame.from_dict(allDownloadableStudies, orient="columns")
    studies.to_csv("studies.csv.gz", compression="gzip", index=False)

    allTagTypes = getAllTagTypes()
    print("Number of tag types:", len(allTagTypes))
    tag_type = pd.DataFrame.from_dict(allTagTypes, orient="columns")
    tag_type.to_csv("tagTypes.csv.gz", compression="gzip", index=False)

    allTaxons = getAllTaxons()
    print("Number of taxons:", len(allTaxons))
    taxons = pd.DataFrame.from_dict(allTaxons, orient="columns")
    taxons.to_csv("taxons.csv.gz", compression="gzip", index=False)

    for study in tqdm.tqdm(allDownloadableStudies):
        study_id = int(study["id"])

        if study_id in downloaded_studies["study_ids"]:
            continue

        try:
            individuals = getIndividualsByStudy(study_id)
            addStudyId(individuals, str(study_id))
            individuals_pd = pd.DataFrame.from_dict(individuals, orient="columns")

            deployment = getDeploymentByStudy(study_id)
            addStudyId(deployment, str(study_id))
            deployment_pd = pd.DataFrame.from_dict(deployment, orient="columns")

            tags = getTagsByStudy(study_id)
            addStudyId(tags, str(study_id))
            tags_pd = pd.DataFrame.from_dict(tags, orient="columns")

            sensors = getSensorsByStudy(study_id)
            addStudyId(sensors, str(study_id))
            sensors_pd = pd.DataFrame.from_dict(sensors, orient="columns")

            events = getEventsByStudy(study_id)
            addStudyId(events, str(study_id))
            events_pd = pd.DataFrame.from_dict(events, orient="columns")

            study_attributes = getAllStudyAttributesByStudy(study_id, set([sensor["sensor_type_id"] for sensor in sensors]))
            study_attributes_pd = pd.DataFrame.from_dict(study_attributes, orient="columns")

            individuals_pd.to_csv("studies/individuals-%d.csv.gz" % study_id, compression="gzip", index=False)
            deployment_pd.to_csv("studies/deployment-%d.csv.gz" % study_id, compression="gzip", index=False)
            tags_pd.to_csv("studies/tags-%d.csv.gz" % study_id, compression="gzip", index=False)
            sensors_pd.to_csv("studies/sensors-%d.csv.gz" % study_id, compression="gzip", index=False)
            events_pd.to_csv("studies/events-%d.csv.gz" % study_id, compression="gzip", index=False)
            study_attributes_pd.to_csv("studies/study_attributes-%d.csv.gz" % study_id, compression="gzip", index=False)

            downloaded_studies["study_ids"].append(study_id)
            json.dump(downloaded_studies, open('downloaded_studies.json', 'w'))
        except:
            pass

    

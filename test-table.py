import argparse
import logging
import os
from google.cloud import bigquery
def create(bq_client,datasetid):
    client = bigquery.Client()
    dataset = datasetid
    dataset_ref = client.dataset(dataset)
    table_name = 'my_table'
    table_ref = dataset_ref.table(table_name)
    table = bigquery.Table(table_ref)
    table = client.create_table(table)

    assert table.table_id == 'my_table'
def run(args):
    bq_client = bigquery.Client(project=args.project)
    create(bq_client,args.datasetid)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help = "Project Identifier")
    parser.add_argument("datasetid", help="Name of the dataset")
   
    logging.getLogger().setLevel(logging.INFO)
    args = parser.parse_args()
    run(args)

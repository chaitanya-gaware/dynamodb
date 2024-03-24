# import json
# import csv
import pandas as pd
import boto3
from datetime import datetime as dt



# define table names -- 1
list_table = ["critical_process", "non_critical_process"]


#defining the client of dynamodb -- 2
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

#function to get the table_list in the dynamodb table
# def get_table_list():
#     list_table = []
#     response = dynamodb.list_tables()
#     tables = response['TableNames']
#     for table in tables:
#         list_table.append(table)
#     return list_table

# function to get the the entries in the dynamodb table 

# def add_entries_dynamodb():
#     table_name = "critical_process"
    
#     data = [
#         {
#             'source_system': {'S': 'alfa'},  # 'S' denotes String data type
#             'file_name_time': {'S': 'file1_time1'},
#             'raw_ingestion_status': {'S': 'Processed'},
#             'inhance_injection': {'S': 'Completed'},
#             'status': {'S': 'Active'},
#             'table_name': {'S': 'SampleTable1'}
#         },
#         {
#             'source_system': {'S': 'alfa'},
#             'file_name_time': {'S': 'file2_time2'},
#             'raw_ingestion_status': {'S': 'Processed'},
#             'inhance_injection': {'S': 'inprogress'},
#             'status': {'S': 'Active'},
#             'table_name': {'S': 'SampleTable2'}
#         },
#         {
#             'source_system': {'S': 'alfa'},
#             'file_name_time': {'S': 'file3_time3'},
#             'raw_ingestion_status': {'S': 'Processed'},
#             'inhance_injection': {'S': 'Fail'},
#             'status': {'S': 'Active'},
#             'table_name': {'S': 'SampleTable3'}
#         },
#         {
#             'source_system': {'S': 'alfa'},
#             'file_name_time': {'S': 'file3_time4'},
#             'raw_ingestion_status': {'S': 'Pending'},
#             'inhance_injection': {'S': 'Fail'},
#             'status': {'S': 'Active'},
#             'table_name': {'S': 'SampleTable4'}
#         }
#     ]

#     # Add the entries to the table with individual error handling
#     for entry in data:
#         try:
#             response = dynamodb.put_item(TableName=table_name, Item=entry)
#         except Exception as e:
#             return print(e)
#     return print("completed")

#function to get the items from the dynamodb table -- 3
def get_entries(table_name):
    try:
        response = dynamodb.scan(
            TableName=table_name
        )
        items = response['Items']
        return items
        # return response
    except Exception as e:
        print("Error:", e)
        return None
    
 #function to convert the output responce of items to pandas df -- 4
def formatted_df_spark(table):
    spark = get_spark_session()
    output_res_items = get_entries(table)
    formatted_data = [{key:value['S'] for key, value in entry.items()} for entry in output_res_items]
    df = spark.createDataFrame(formatted_data)
    return df


def get_spark_session():
    # Import required modules
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col
    # from pyspark.sql.types import *

    # Create a SparkSession       
    return SparkSession.builder \
        .appName("YourAppName") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    

# def lambda_handler(): 
    
#     table = dynamodb.Table("critical_process")
    
#     response = dynamodb.list_tables()
#     table_names = response['TableNames']

#     # Print table names
#     print("DynamoDB Tables:")
#     for table_name in table_names:
#         print(table_name)
#     return print("process sucess")





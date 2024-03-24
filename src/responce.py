from lambda_function import *


#=============== calling lambda handler ==================
# res = lambda_handler()
# print(res)

#### ============ calling the table list ================
# res = get_table_list()
# print(res)

#================calling add entries in the table =======
# res_table_entries = add_entries_dynamodb()
# print(res_table_entries)


#============== getting entries from the table =============
# -- 5 
for table in list_table:
    panda_df = formatted_df_panda(table)
    print(panda_df)
    # break;
# =================
  
## -- 6 convert pandas dataframe to pyspark 
## -- 7  widgets 
## --8 date time module define define the when the job is run 
## -- 9 write pyspark dataframe to edl table
          
        

import json
import azure.functions as func
from azure.data.tables import TableServiceClient
from azure.data.tables import UpdateMode
import os
 
app = func.FunctionApp()

@app.route(route="theshow")
def table_in_binding(req: func.HttpRequest):
    connection_string = os.environ["HomerunCosmosConnection"] 

    with TableServiceClient.from_connection_string(conn_str=connection_string) as table_service_client:

        table = table_service_client.get_table_client("homeruntable") # This creates an instance of the client(table) to interact with it

        existing_entity = table.get_entity(
            row_key="Astros",
            partition_key="Yordan",
        )
        new_homeruns = existing_entity.get("Homeruns") 	# grab the value of key homeruns
        new_count = new_homeruns + 1 					# update the homeruns count
        existing_entity["Homeruns"] = new_count			# update the value of key 'homeruns' in the dictionary

        table.upsert_entity(mode=UpdateMode.REPLACE, entity=existing_entity) # return the new dictionary with the update value for key 'homeruns'
        print(f"New homerun count is at {new_count}")    
        
        new_homer_dict = {"Homeruns": new_count}
        
        json_string = json.dumps(new_homer_dict)    #output is {"Homeruns": int} which future JS reads with data.Homeruns
        
        return func.HttpResponse(json_string)  
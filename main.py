import os
from dotenv import load_dotenv
from src.lucca.lucca_client import LuccaClient
from src.helpers.helpers import export_data_to_json, yaml_fields_to_lucca_str, load_yaml_config, apply_schema

def main():

    load_dotenv()
    api_host = os.getenv("API_HOST")
    api_key = os.getenv("API_KEY")
    storage_folder = os.getenv("STORAGE_FOLDER")
    config_file = os.getenv("CONFIG_FILE")

    lucca = LuccaClient(
        host=api_host,
        api_key=api_key
    )

    #Récupération de la config
    config_yaml = load_yaml_config(config_file)

    for collection, config in config_yaml.items():
        # Récupération des informations du fichier config.yaml
        collection_endpoint = config.get("endpoint")
        collection_params = config.get("params")
        collection_type = config.get("type")
        collection_output_schema = config.get("output_schema")
        collection_file_name = config.get("file_name", f"{collection}.json")

        #Transformation de la liste de champs en une chaîne de caractères
        if collection_params and collection_params.get("fields"):
            collection_params["fields"] = yaml_fields_to_lucca_str(collection_params["fields"])

        print(f"=========================\nStart processing data for {collection} - {collection_endpoint}")
        print(f"Parameters: {collection_params}")
        print(f"schema: {collection_output_schema}")
        try:
            #Extraction des données
            if collection_type == 'items':
                data = lucca.get_all_paginated_items(collection_endpoint, collection_params)
            elif collection_type == 'itemless':
                data = lucca.get_itemless_data(collection_endpoint, collection_params)
            else:
                print(f"No collection type for {collection} - extraction abort")

        except Exception as e:
            print(f"Error while extracting {collection}: {e}")
            continue

        if data:
            print("Defining schema...")
            #Définition du schéma
            try:
                results = apply_schema(collection_output_schema, data)

            except Exception as e:
                print(f"Error in output schema filter for {collection}: {e}")
                continue

            #Export des données au format JSON
            try:
                export_data_to_json(results, collection_file_name, storage_folder)
                print(f"Exported {len(data)} rows to {collection_file_name}\n")
            except Exception as e:
                print(f"Error during data json export for {collection}: {e}")

        else:
            print(f"No data extracted for {collection}\n")

if __name__ == "__main__":
    main()
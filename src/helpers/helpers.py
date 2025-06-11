import json
import os
import yaml
from src.schemas import SCHEMA_MAP

def export_data_to_json(data, file_name, destination_path):
    """
        Exporte les données au format json
    """
    try:
        full_path = os.path.join(destination_path, file_name)
        print(f"Exporting data to : {full_path}")

        with open(full_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print(f"Data exported successfully to {full_path}")
    except Exception as e:
        print(f"Failed to export data: {e}")

def yaml_fields_to_lucca_str(fields: list) -> str:
    """
        Récupère et transforme une liste de champs en une liste de format string compréhensible pour l'api Lucca:
        https://developers.lucca.fr/api-reference/legacy/api-generations Cf.Expanding responses
    """
    final_list = []
    for field in fields:
        if isinstance(field, dict):
            for key, value in field.items():
                nested_fields = yaml_fields_to_lucca_str(value)
                final_list.append(f"{key}[{nested_fields}]")
        else:
            final_list.append(field)
    return ",".join(final_list)

def load_yaml_config(path):
    """
        Permet de lire un fichier YAML pour un path donné.
    """
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def apply_schema(schema_name: str, data):
    """
        Sélectionne et applique le schéma aux données
    """
    schema_func = SCHEMA_MAP.get(schema_name)
    if not schema_func:
        raise ValueError(f"function not found for '{schema_name}'")
    if isinstance(data, list):
        return [schema_func(item) for item in data]
    else:
        return schema_func(data)
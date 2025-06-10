from .department_schema import department_schema
from .user_schema import user_schema
from .work_contract_schema import work_contract_schema

SCHEMA_MAP = {
    "department_schema": department_schema,
    "user_schema": user_schema,
    "work_contract_schema": work_contract_schema
}
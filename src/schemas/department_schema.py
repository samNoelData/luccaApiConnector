def department_schema(department: dict) -> dict:
    """
        Schéma pour les données concernant la collection 'departments'
    """
    return {
        "id": department.get("id"),
        "name": department.get("name"),
        "code": department.get("code"),
        "hierarchy": department.get("hierarchy"),
        "parentId": department.get("parentId"),
        "level": department.get("level"),
        "isActive": department.get("isActive"),
        "headID": department.get("headID"),
        "users": [
            {
                "id": department.get("id"),
                "name": department.get("name")
            } for department in department.get("users", [])
        ] or None,
        "currentUsers": [
            {
                "id": department.get("id"),
                "name": department.get("name")
            } for department in department.get("currentUsers", [])
        ] or None,
        "currentUsersCount": department.get("currentUsersCount")
    }
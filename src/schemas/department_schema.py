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
                "id": user.get("id"),
                "name": user.get("name")
            } for user in department.get("users", [])
        ] or None,
        "currentUsers": [
            {
                "id": currentUser.get("id"),
                "name": currentUser.get("name")
            } for currentUser in department.get("currentUsers", [])
        ] or None,
        "currentUsersCount": department.get("currentUsersCount")
    }
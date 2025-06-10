def user_schema(user: dict) -> dict:
    """
        Schéma pour les données concernant la collection 'users'
    """
    return {
        "id": user.get("id"),
        "firstName": user.get("firstName"),
        "lastName": user.get("lastName"),
        "gender": user.get("gender"),
        "birthDate": user.get("birthDate"),
        "nationalityId": user.get("nationalityId"),
        "address": user.get("address"),
        "insuranceNumber": user.get("insuranceNumber"),
        "culture": {
            "id": (user.get("culture") or {}).get("id"),
            "name": (user.get("culture") or {}).get("name")
        },
        "calendar": {
            "id": (user.get("calendar") or {}).get("id"),
            "name": (user.get("calendar") or {}).get("name")
        },
        "employeeNumber": user.get("employeeNumber"),
        "mail": user.get("mail"),
        "personalEmail": user.get("personalEmail"),
        "jobTitle": user.get("jobTitle"),
        "legalEntityID": user.get("legalEntityID"),
        "departmentID": user.get("departmentID"),
        "managerID": user.get("managerID"),
        "rolePrincipal": {
            "id": (user.get("rolePrincipal") or {}).get("id"),
            "name": (user.get("rolePrincipal") or {}).get("name")
        },
        "habilitedRoles": [
                {
                    "id": role.get("id"),
                    "name": role.get("name")
                } for role in user.get("habilitedRoles", [])
        ] or None,
        "bankName": user.get("bankName"),
        "allowsElectronicPayslip": user.get("allowsElectronicPayslip"),
        "frenchCarTaxHorsePower": user.get("frenchCarTaxHorsePower"),
        "frenchMotocyclesTaxHorsePower": user.get("frenchMotocyclesTaxHorsePower"),
        "userWorkCycles": [
            {
                "id": cycle.get("id"),
                "workCycleID": cycle.get("workCycleID"),
                "startsOn": cycle.get("startsOn"),
                "endsOn": cycle.get("endsOn")
            } for cycle in user.get("userWorkCycles", [])
        ] or None,
        "applicationData": {
            "profile_figgo": {
                "id": ((user.get("applicationData") or {}).get("profile_figgo") or {}).get("id"),
                "name": ((user.get("applicationData") or {}).get("profile_figgo") or {}).get("name")
            }
        }
    }
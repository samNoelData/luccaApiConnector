def work_contract_schema(work_contract: dict) -> dict:
    """
        Schéma pour les données concernant la collection 'work_contracts'
    """
    return {
        "id": work_contract.get("id"),
        "ownerId": work_contract.get("ownerId"),
        "startsOn": work_contract.get("startsOn"),
        "endsOn": work_contract.get("endsOn"),
        "isApplicable": work_contract.get("isApplicable"),
        "establishmentId": work_contract.get("establishmentId"),
        "spc": {
            "id": (work_contract.get("spc") or {}).get("id"),
            "name": (work_contract.get("spc") or {}).get("name")
        },
        "type": {
            "id": (work_contract.get("type") or {}).get("id"),
            "name": (work_contract.get("type") or {}).get("name")
        },
        "hiringType": {
            "id": (work_contract.get("hiringType") or {}).get("id"),
            "name": (work_contract.get("hiringType") or {}).get("name")
        },
        "terminationReason": {
            "id": (work_contract.get("terminationReason") or {}).get("id"),
            "name": (work_contract.get("terminationReason") or {}).get("name")
        },
        "trialPeriodDays": work_contract.get("trialPeriodDays"),
        "renewedTrialPeriodDays": work_contract.get("renewedTrialPeriodDays"),
        "trialPeriodEndDate": work_contract.get("trialPeriodEndDate"),
        "trialPeriodEndDate2": work_contract.get("trialPeriodEndDate2"),
        "authorId": work_contract.get("authorId"),
        "lastModifierId": work_contract.get("lastModifierId"),
        "createdAt": work_contract.get("createdAt"),
        "lastModifiedAt": work_contract.get("lastModifiedAt"),
        "temporaryContractGroundId": work_contract.get("temporaryContractGroundId"),
        "internshipSupervisorId": work_contract.get("internshipSupervisorId")
    }
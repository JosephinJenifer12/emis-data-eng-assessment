observation_mapping = {
    "ObservationGuid": "resource.id",
    "PatientGuid": "resource.subject.reference",
    # EncounterGuid: "resource.encounter.reference",
    "Status": "resource.status",
    "EffectiveDateTime": "resource.effectiveDateTime",
    "IssuedDateTime": "resource.issued",
    "Category": "resource.category[0].codeing[0].display",
    "Code": "resource.code.coding[0].code",
    "Description": "resource.code.coding[0].display",
    "Value": "resource.valueQuantity.value",
    "Unit": "resource.valueQuantity.unit"
}
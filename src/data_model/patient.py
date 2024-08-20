
mapping = {
    "PatientGuid": "resource.id",
    "Gender": "resource.gender",
    "BirthDate": "resource.birthDate",
    "MultipleBirthBoolean": "resource.multipleBirthBoolean",
    "FamilyName": "resource.name[0].family",   # First entry in the name list
    "GivenName": "resource.name[0].given[0]",  # First given name from the first name entry
    "Prefix": "resource.name[0].prefix[0]",    # First prefix from the first name entry
    "BirthPlaceCity": "resource.extension[4].valueAddress.city",  # City from the birthPlace extension
    "BirthPlaceState": "resource.extension[4].valueAddress.state",  # State from the birthPlace extension
    "BirthPlaceCountry": "resource.extension[4].valueAddress.country",  # Country from the birthPlace extension
    "DisabilityAdjustedLifeYears": "resource.extension[5].valueDecimal",  # Disability adjusted life years
    "QualityAdjustedLifeYears": "resource.extension[6].valueDecimal"  # Quality adjusted life years
}
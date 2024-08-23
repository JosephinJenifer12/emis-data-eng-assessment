patient_mapping = {
    "PatientGuid": "resource.id",
    "Gender": "resource.gender",
    "BirthDate": "resource.birthDate",
    "MultipleBirthBoolean": "resource.multipleBirthBoolean",
    "DeceasedDateTime": "resource.deceasedDateTime",
    "FamilyName": "resource.name[0].family",   # First entry in the name list
    "GivenName": "resource.name[0].given[0]",  # First given name from the first name entry
    "Prefix": "resource.name[0].prefix[0]",    # First prefix from the first name entry
    "Race": "resource.extension[0].extension[1].valueString", # Race from the extension
    "Ethnicity": "resource.extension[1].extension[1].valueString", # Ethinicity from the extension
    "MothersMaidenName": "resource.extension[2].valueString", # Mothers Maiden Name from the extension
    "BirthSex": "resource.extension[3].valueCode", # Birth Sex from the extension
    "BirthPlaceCity": "resource.extension[4].valueAddress.city",  # City from the birthPlace extension
    "BirthPlaceState": "resource.extension[4].valueAddress.state",  # State from the birthPlace extension
    "BirthPlaceCountry": "resource.extension[4].valueAddress.country",  # Country from the birthPlace extension
    "DisabilityAdjustedLifeYears": "resource.extension[5].valueDecimal",  # Disability adjusted life years
    "QualityAdjustedLifeYears": "resource.extension[6].valueDecimal",  # Quality adjusted life years
    "CurrentAddress": "resource.address[0].line[0]", # First entry of the address line from the geolocation
    "CurrentAddressCity": "resource.address[0].city", # City from the goelocation
    "CurrentAddressState": "resource.address[0].state", # State from the goelocation
    "CurrentAddressCountry": "resource.address[0].country", # Country from the goelocation
    "MaritalStatus": "resource.maritalStatus.text", #Marital status,
    "CommunicationLanguage": "resource.communication[0].language.text", # Medium of language preferred for the communication
    "HomePhone": "resource.telecom[0].value", # home phone number to be contacted
    "SSN": "resource.identifier[2].value", # SSN number from the identifier
    "DrivingLicence": "resource.identifier[3].value", # Driver's licence number from the identifier
    "PassportNumber": "resource.identifier[4].value", # Passport number from the identifier

}
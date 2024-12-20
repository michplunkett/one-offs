"""Contains any constants that may be used in more than one package."""

# Misc.
ENCODING_STANDARD = "utf-8"
STANDARD_DPI = 720

# File open
FILE_OPEN_MODE_READ = "r"
FILE_OPEN_MODE_WRITE = "w"

# File types
FILE_TYPES_CSV = "csv"
FILE_TYPES_JPEG = "jpeg"
FILE_TYPES_PDF = "pdf"
FILE_TYPES_TXT = "txt"

# File extensions
EXTENSION_CSV = "." + FILE_TYPES_CSV
EXTENSION_JPEG = "." + FILE_TYPES_JPEG
EXTENSION_PDF = "." + FILE_TYPES_PDF
EXTENSION_TXT = "." + FILE_TYPES_TXT

# API constants
SLEEP_TIME_ERROR = 1

# ISO 639-1 language codes
ISO_LANGUAGES = [
    "aa",
    "ab",
    "af",
    "ak",
    "sq",
    "am",
    "ar",
    "an",
    "hy",
    "as",
    "av",
    "ae",
    "ay",
    "az",
    "ba",
    "bm",
    "eu",
    "be",
    "bn",
    "bh",
    "bi",
    "bo",
    "bs",
    "br",
    "bg",
    "my",
    "ca",
    "cs",
    "ch",
    "ce",
    "zh",
    "cu",
    "cv",
    "kw",
    "co",
    "cr",
    "cy",
    "cs",
    "da",
    "de",
    "dv",
    "nl",
    "dz",
    "el",
    "en",
    "eo",
    "et",
    "eu",
    "ee",
    "fo",
    "fa",
    "fj",
    "fi",
    "fr",
    "fy",
    "ff",
    "Ga",
    "de",
    "gd",
    "ga",
    "gl",
    "gv",
    "el",
    "gn",
    "gu",
    "ht",
    "ha",
    "he",
    "hz",
    "hi",
    "ho",
    "hr",
    "hu",
    "hy",
    "ig",
    "is",
    "io",
    "ii",
    "iu",
    "ie",
    "ia",
    "id",
    "ik",
    "is",
    "it",
    "jv",
    "ja",
    "kl",
    "kn",
    "ks",
    "ka",
    "kr",
    "kk",
    "km",
    "ki",
    "rw",
    "ky",
    "kv",
    "kg",
    "ko",
    "kj",
    "ku",
    "lo",
    "la",
    "lv",
    "li",
    "ln",
    "lt",
    "lb",
    "lu",
    "lg",
    "mk",
    "mh",
    "ml",
    "mi",
    "mr",
    "ms",
    "Mi",
    "mk",
    "mg",
    "mt",
    "mn",
    "mi",
    "ms",
    "my",
    "na",
    "nv",
    "nr",
    "nd",
    "ng",
    "ne",
    "nl",
    "nn",
    "nb",
    "no",
    "oc",
    "oj",
    "or",
    "om",
    "os",
    "pa",
    "fa",
    "pi",
    "pl",
    "pt",
    "ps",
    "qu",
    "rm",
    "ro",
    "ro",
    "rn",
    "ru",
    "sg",
    "sa",
    "si",
    "sk",
    "sk",
    "sl",
    "se",
    "sm",
    "sn",
    "sd",
    "so",
    "st",
    "es",
    "sq",
    "sc",
    "sr",
    "ss",
    "su",
    "sw",
    "sv",
    "ty",
    "ta",
    "tt",
    "te",
    "tg",
    "tl",
    "th",
    "bo",
    "ti",
    "to",
    "tn",
    "ts",
    "tk",
    "tr",
    "tw",
    "ug",
    "uk",
    "ur",
    "uz",
    "ve",
    "vi",
    "vo",
    "cy",
    "wa",
    "wo",
    "xh",
    "yi",
    "yo",
    "za",
    "zh",
    "zu",
]

# Incident Category Lists
INCIDENT_CATS_MISC = [
    "Accident Report",
    "Accidental Fire",
    "Accidental Injury",
    "Accidental Shooting",
    "Accidental",
    "Aggravated Fleeing Police",
    "Alarm",
    "Ambulance Request",
    "Animal Bite",
    "Arrest on Warrant",
    "Arrest",
    "Arson by Fire",
    "Arson",
    "Assault and Harassment by Electronic Means",
    "Assist Other Agency Motor Vehicle Theft and Recovery",
    "Assist Other Agency",
    "Attempt",
    "Attempted Suicide",
    "Attempted",
    "Automobile",
    "Bomb Threat",
    "Burglary",
    "Chemical Spill",
    "Child Abandonment",
    "Computer Fraud",
    "Counterfeit Check",
    "Counterfeit Document",
    "Credit Card Fraud",
    "Criminal Damage to Motor Vehicle",
    "Criminal Damage to Property",
    "Criminal Damage to Vehicle",
    "Criminal Defacement",
    "Criminal Trespass to Land",
    "Criminal Trespass to Motor Vehicle",
    "Criminal Trespass to Property",
    "Criminal Trespass to Residence",
    "Criminal Trespass to Vehicle",
    "Criminal Trespass",
    "Cutting Instrument",
    "Cyber Scam",
    "Cyberstalking",
    "DUI Arrest",
    "DUI",
    "Damage to City Property",
    "Damage to Personal Property",
    "Damage to Property",
    "Damage to UC Property",
    "Damage to UC Vehicle",
    "Damage to Vehicle",
    "Damage",
    "Damaged Property",
    "Death Investigation",
    "Deceptive Practice",
    "Deceptive",
    "Defacement",
    "Delayed Burglary",
    "Delayed Report",
    "Delayed Robbery",
    "Delayed",
    "Disorderly Conduct",
    "Disturbance",
    "Dog Bite",
    "Eavesdropping",
    "Electronic Means",
    "Elevator Entrapment",
    "Eluding Police",
    "Expired License",
    "Extortion",
    "Failure to Register",
    "False Fire Alarm",
    "False Police Report",
    "Financial Identity Theft",
    "Fire Alarm",
    "Fire",
    "Fleeing Police",
    "Fleeing or Attempting to Elude Police",
    "Fleeing",
    "Foreign Steal",
    "Forged Prescription",
    "Forgery",
    "Found Key",
    "Found Person",
    "Found Property",
    "Found Wallet",
    "Found Weapon",
    "Found",
    "Fraud",
    "Fraudulent Check",
    "Harassing Email Message",
    "Harassing Email",
    "Harassing Message",
    "Harassing Phone Call",
    "Harassing Telephone Call",
    "Harassment Via Electronic Means",
    "Harassment by Electronic Means",
    "Harassment by Telephone",
    "Haz Mat Event",
    "Haz Mat Incident",
    "Haz Mat",
    "Haz-Mat Incident",
    "Hazardous Material Event",
    "Hazardous Material Incident",
    "Hit and Run Property Damage",
    "Hit and Run Traffic Crash",
    "Identity Theft",
    "Ill Person",
    "Illegal Consumption by Minor",
    "Illegal Possession of Cash Card",
    "Illness",
    "Impersonation",
    "Information Criminal Damage to Property",
    "Information Harassment",
    "Information Report",
    "Injured Person",
    "Interference with Police Officer",
    "Interference with Public Officer",
    "Interfering",
    "Intimidation",
    "Irregular Condition",
    "Liquor Law Violation",
    "Lost Phone",
    "Lost Property",
    "Lost Wallet",
    "Lost",
    "Medical Call",
    "Medical Illness",
    "Medical Transport",
    "Mental Health Call",
    "Mental Health Transport",
    "Mental Health",
    "Mental Transport",
    "Minor Injury",
    "Minor Personal Injury",
    "Miscellaneous Incident Report",
    "Miscellaneous Incident",
    "Miscellaneous",
    "Mislaid Property",
    "Missing Person Found",
    "Missing Person",
    "Missing Property",
    "Motor Vehicle Accident",
    "Motor Vehicle Recovery",
    "Motor Vehicle Theft Recovery",
    "Motor Vehicle Theft and Recovery",
    "Motor Vehicle Theft",
    "Noise Complaint",
    "Non-Criminal Complaint",
    "Non-Criminal Damage to Property",
    "Non-Criminal Damage to Vehicle",
    "Non-Criminal Damage",
    "Non-Criminal Event",
    "Non-Criminal Fire",
    "Non-Criminal Incident",
    "Non-Criminal Informational Report",
    "Non-Criminal Missing Property",
    "Non-Criminal Offense",
    "Non-Criminal Other",
    "Non-Criminal Property Damage",
    "Non-Criminal Property",
    "Non-Criminal Report",
    "Non-Criminal",
    "Non-Forcible",
    "Notice of Order of Protection",
    "Notification of Order of Protection",
    "Notification",
    "Obscene Phone Call",
    "Obstruct Police Officer",
    "Obstructing Peace Officer",
    "Obstructing Police",
    "Obstructing Traffic",
    "Obstructing a Peace Officer",
    "Obstructing a Police Officer",
    "Order of Protection Arrest",
    "Order of Protection Notification",
    "Order of Protection",
    "Other Crime Vs. Person",
    "Other Crime against Person",
    "Other Crime",
    "Other Dangerous Weapon",
    "Other Deadly Weapon",
    "Other Non-Criminal Property",
    "Other Offense",
    "Other Vehicle Offense",
    "Other Violation",
    "Other",
    "Outside Agency Warrant Arrest",
    "Pedestrian",
    "Person Down",
    "Personal Injury",
    "Personation of Peace Officer",
    "Police Officer",
    "Possession of Lost",
    "Possession of Stolen Motor Vehicle",
    "Possession of Stolen Property",
    "Prohibited Zone",
    "Property Damage Only",
    "Property Damage",
    "Property",
    "Public Indecency",
    "Public Peace Violation",
    "Public Way",
    "Rear of Apt. Building",
    "Reckless Conduct",
    "Reckless Driving",
    "Recovered Firearm",
    "Recovered Motor Vehicle",
    "Recovered Property",
    "Recovered Stolen Motor Vehicle",
    "Recovered Stolen Vehicle",
    "Recovered Vehicle Plate",
    "Recovered Vehicle",
    "Recovery of Motor Vehicle",
    "Recovery",
    "Resisting Arrest",
    "Resisting Police",
    "Safety Hazard",
    "Security Alarm",
    "Senior Citizen",
    "Sick Person",
    "Simple",
    "Smell of Gas",
    "Smoke Alarm",
    "Smoke",
    "Stolen Motor Vehicle Recovery",
    "Stolen Vehicle Recovery",
    "Stuck Elevator",
    "Suspicious Activity",
    "Suspicious Letter",
    "Suspicious Mail",
    "Suspicious Package",
    "Suspicious Person",
    "Suspicious Phone Call",
    "Suspicious Vehicle",
    "Telephone Harassment",
    "Telephone Scam",
    "Telephone Threat",
    "Theft and Recovery of Motor Vehicle",
    "Theft by Deception",
    "Theft from Motor Vehicle",
    "Theft from Vehicle",
    "Theft of Lost Property",
    "Theft of Lost Property",
    "Theft of Lost or Mislaid Property",
    "Theft of Lost",
    "Theft of Motor Vehicle",
    "Theft of Motorcycle",
    "Theft of Service",
    "Theft",
    "Threat by Electronic Means",
    "Threatening Call",
    "Threatening Phone Call",
    "Traffic Accident",
    "Traffic Arrest",
    "Traffic Collision",
    "Traffic Crash Arrest",
    "Traffic Crash Hit and Run",
    "Traffic Crash Property Damage",
    "Traffic Crash Report",
    "Traffic Crash",
    "Traffic Offense",
    "Traffic Violation Arrest",
    "Traffic Violation and Warrant Arrest",
    "Traffic Violation",
    "Traffic and Warrant Arrest",
    "Traffic",
    "Trespass Warning",
    "Trespass to Land",
    "Trespass to Motor Vehicle",
    "Trespass to Property",
    "Trespass to Vehicle",
    "Trespass",
    "UCPD Arrest Warrant",
    "Unauthorized Use of Computer",
    "Unlawful Possession of Ammunition",
    "Unlawful Possession of Firearm",
    "Unlawful Possession of Weapon",
    "Unlawful Possession of a Firearm",
    "Unlawful Possession of a Handgun",
    "Unlawful Possession of a Weapon",
    "Unlawful Restraint",
    "Vandalism",
    "Vehicle Crash",
    "Vehicle Fire",
    "Vehicle Recovery",
    "Vehicle Theft and Recovery",
    "Warrant Arrest",
    "Warrant",
    "Weapon Arrest",
    "Weapon Recovery",
    "Weapon Turn-In",
    "Weapon Violation",
    "Well-Being Check",
    "Well-Being",
]

INCIDENT_CATS_NARCOTICS = [
    "Deliver Narcotic",
    "Delivery of Cannabis",
    "Drug Law Violation",
    "Found Drug Paraphernalia",
    "Found Narcotic Paraphernalia",
    "Found Narcotic",
    "Found Suspect Marijuana",
    "Found Suspect Narcotic",
    "Narcotic Arrest",
    "Narcotic Delivery",
    "Narcotic",
    "Possession of Cannabis",
    "Possession of Controlled Substance",
    "Possession of Crack Cocaine",
    "Possession of Drug Paraphernalia",
    "Possession of Marijuana",
    "Possession of Narcotic with Intent to Deliver",
    "Possession of Narcotic",
    "Possession of a Controlled Substance",
    "Suspect Narcotic Found",
    "Suspect Narcotic",
]

INCIDENT_CATS_SEX_ASSAULT_GENDER = [
    "Aggravated Criminal Sexual Assault",
    "Aggravated Domestic Assault",
    "Aggravated Domestic Battery",
    "Attempted Sexual Assault",
    "Criminal Sexual Abuse",
    "Criminal Sexual Assault",
    "Dating Violence",
    "Domestic Aggravated Assault",
    "Domestic Aggravated Battery",
    "Domestic Assault",
    "Domestic Battery",
    "Domestic Dispute",
    "Domestic Disturbance",
    "Domestic Issue",
    "Domestic",
    "Fondling",
    "Indecent Exposure",
    "Luring a Minor",
    "Sex Crime",
    "Sex Offender",
    "Sex Offense",
    "Sex Related",
    "Sexual Abuse",
    "Sexual Assault",
    "Stalking",
    "Violation of Order of Protection",
]

INCIDENT_CATS_VIOLENCE = [
    "Aggravated Assault of Police Officer",
    "Aggravated Assault of a Police Officer",
    "Aggravated Assault",
    "Aggravated Battery of Police Officer",
    "Aggravated Battery of a Police Officer",
    "Aggravated Battery of a Protected Employee",
    "Aggravated Battery to Police Officer",
    "Aggravated Battery",
    "Aggravated Discharge of a Firearm",
    "Aggravated Robbery",
    "Aggravated Vehicular Carjacking",
    "Aggravated Vehicular Hijacking",
    "Armed Robbery Arrest",
    "Armed Robbery",
    "Assault",
    "Attempted Aggravated Robbery",
    "Attempted Aggravated Vehicular Hijacking",
    "Attempted Armed Robbery",
    "Attempted Burglary",
    "Attempted Home Invasion",
    "Attempted Motor Vehicle Theft",
    "Attempted Robbery",
    "Attempted Strong Arm",
    "Attempted Theft from Motor Vehicle",
    "Attempted Theft from Person",
    "Attempted Theft of Motor Vehicle",
    "Attempted Theft",
    "Attempted Vehicular Hijacking",
    "Battery of Police Officer",
    "Battery of a Police Officer",
    "Battery to Police Officer",
    "Battery",
    "Battery-Simple",
    "Carjacking",
    "Harassment",
    "Hate Crime",
    "Hit and Run",
    "Home Invasion",
    "Homicide",
    "Murder",
    "Purse Snatch",
    "Reckless Discharge of Firearm",
    "Reckless Discharge of a Firearm",
    "Reckless Discharge of a Weapon",
    "Robbery Arrest",
    "Robbery",
    "Robbery-Aggravated",
    "Robbery-Strong Arm",
    "Shooting",
    "Shot Fired",
    "Simple Assault Battery",
    "Simple Assault",
    "Simple Battery",
    "Strong Arm",
    "Strong Armed",
    "Theft from Person",
    "Threat",
    "Unlawful Discharge of Firearm",
    "Unlawful Discharge of Weapon",
    "Unlawful Discharge of a Firearm",
    "Unlawful Discharge of a Weapon",
    "Unlawful Use of Firearm",
    "Unlawful Use of Weapon",
    "Unlawful Use of a Firearm",
    "Unlawful Use of a Weapon Arrest",
    "Unlawful Use of a Weapon",
    "Vehicle Hijacking",
    "Vehicular Carjacking",
    "Vehicular Hijacking",
]

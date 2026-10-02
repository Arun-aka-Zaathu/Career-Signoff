# ==================================================
# CareerSignoff Configuration File
# ==================================================

# Application Information

APP_NAME = "CareerSignoff"


# ==================================================
# Input File Rules
# ==================================================

REQUIRED_FILE_TYPE = ".xlsx"


# ==================================================
# Required Excel Sheets
# ==================================================

REQUIRED_SHEETS = [
    "Application Tracker",
    "Target Companies Database",
    "Recruiter Contact",
    "Skill Tracker"
]


# ==================================================
# Application Tracker Mandatory Columns
# ==================================================

APPLICATION_TRACKER_COLUMNS = [
    "Date Applied",
    "Company",
    "Country",
    "Role",
    "Status",
    "Priority"
]
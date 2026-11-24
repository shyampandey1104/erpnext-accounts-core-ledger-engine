# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "accounts_core"
app_title = "Erpnext Accounts Core Ledger Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Accounts Core Ledger Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/accounts_core/css/accounts_core.bundle.css"
app_include_js = "/assets/accounts_core/js/accounts_core.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Accounts Core Ledger Engine Entry": {
        "validate": "accounts_core.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "accounts_core.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "accounts_core.tasks.hourly_sync"
    ],
    "daily": [
        "accounts_core.tasks.daily_reconciliation"
    ],
    "weekly": [
        "accounts_core.tasks.weekly_digest"
    ]
}

[automation-scripts-README.txt](https://github.com/user-attachments/files/30128978/automation-scripts-README.txt)
# automation-scripts# automation-scripts

> A toolkit of Python automation scripts for report generation, email dispatch, file processing, API integrations, and scheduled task workflows.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Scheduled](https://img.shields.io/badge/Scheduling-cron%20%7C%20Task%20Scheduler-555555?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

---

## Overview

A production-ready collection of Python automation scripts that eliminate repetitive manual work. Each script is standalone, config-driven, and built to run unattended on a schedule — whether via Windows Task Scheduler, cron, or an orchestration tool like Airflow.

Built for businesses that spend hours each week on tasks a script could handle in seconds.

---

## Script Categories

| Category | Scripts | Business Use Case |
|---|---|---|
| **Reporting** | Auto report generator, email sender, Excel builder | Replace manual weekly/monthly report creation |
| **File Processing** | Batch renamer, CSV merger, PDF extractor | Automate file management and data prep |
| **API Integrations** | Salesforce sync, Google Sheets writer, Slack notifier | Keep systems in sync without manual exports |
| **Scheduling** | Windows Task Scheduler setup, cron wrapper | Deploy automations as reliable scheduled jobs |
| **Database** | DB backup, query runner, connection manager | Automate database ops and data extracts |

---

## Project Structure

```
automation-scripts/
├── README.md
├── requirements.txt
├── .env.example
├── reporting/
│   ├── auto_report_generator.py       # Build formatted reports from any data source
│   ├── email_report_sender.py         # Send reports via SMTP with attachments
│   └── excel_report_builder.py        # Create styled Excel reports with openpyxl
├── file_processing/
│   ├── batch_file_renamer.py          # Rename files in bulk using pattern rules
│   ├── csv_merger.py                  # Merge multiple CSVs with schema validation
│   └── pdf_extractor.py              # Extract text/tables from PDFs to DataFrame
├── api_integrations/
│   ├── salesforce_sync.py            # Pull/push data via Salesforce REST API
│   ├── google_sheets_writer.py       # Write DataFrames to Google Sheets
│   └── slack_notifier.py             # Send alerts and reports to Slack channels
├── scheduling/
│   ├── windows_task_scheduler_setup.py  # Register scripts as Windows scheduled tasks
│   └── cron_wrapper.py               # Shell wrapper with logging for cron jobs
├── database/
│   ├── db_backup.py                  # Automated PostgreSQL / SQL Server backups
│   ├── query_runner.py               # Run parameterized SQL queries from config
│   └── connection_manager.py         # Centralized DB connection pool
└── utils/
    ├── logger.py                     # Rotating file logger with email alerts on error
    ├── config_loader.py              # Load and validate config from YAML + .env
    └── email_client.py               # SMTP email client with attachment support
```

---

## Highlighted Automations

### 📊 Automated Report Pipeline

| | |
|---|---|
| **Problem** | Analyst spends 3 hours every Monday building and emailing a sales report |
| **Solution** | `auto_report_generator.py` pulls data → `excel_report_builder.py` formats it → `email_report_sender.py` delivers it |
| **Schedule** | Every Monday at 7 AM via cron or Task Scheduler |
| **Time saved** | ~3 hours/week |

---

### 🔄 Salesforce → Data Warehouse Sync

| | |
|---|---|
| **Problem** | Ops team manually exports Salesforce reports to CSV and uploads to SQL Server daily |
| **Solution** | `salesforce_sync.py` pulls via API → `connection_manager.py` + `query_runner.py` upsert to warehouse |
| **Schedule** | Nightly at 11 PM |
| **Time saved** | ~45 minutes/day |

---

### 📁 Batch File Processing

| | |
|---|---|
| **Problem** | Hundreds of CSV exports from a legacy system need to be renamed, merged, and loaded each week |
| **Solution** | `batch_file_renamer.py` standardizes names → `csv_merger.py` consolidates → ETL pipeline picks up |
| **Schedule** | Triggered on file-drop or scheduled daily |
| **Time saved** | ~2 hours/week |

---

### 🔔 Slack Alert System

| | |
|---|---|
| **Problem** | Team only finds out about pipeline failures when someone notices missing data |
| **Solution** | `slack_notifier.py` integrated into all scripts — sends success/failure alerts to a #data-ops channel |
| **Schedule** | Triggered on script completion or error |
| **Time saved** | Hours of troubleshooting from late detection |

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/jeff-rotar/automation-scripts
cd automation-scripts

# Set up environment
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials

# Run any script directly
python reporting/auto_report_generator.py --config config.yaml

# Schedule with cron (Linux/macOS)
crontab -e
# Add: 0 7 * * 1 /path/to/venv/python /path/to/reporting/auto_report_generator.py

# Schedule with Windows Task Scheduler
python scheduling/windows_task_scheduler_setup.py --script reporting/auto_report_generator.py --time 07:00
```

---

## Configuration

All scripts read from `.env` and optionally from a `config.yaml`:

```
# .env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@email.com
SMTP_PASSWORD=your_app_password

DB_HOST=localhost
DB_NAME=your_database
DB_USER=db_user
DB_PASSWORD=db_password

SLACK_BOT_TOKEN=xoxb-your-token
SLACK_CHANNEL=#data-ops

SALESFORCE_USERNAME=your@sf.com
SALESFORCE_PASSWORD=your_password
SALESFORCE_TOKEN=your_security_token

GOOGLE_SHEETS_CREDS=path/to/credentials.json
```

---

## Prerequisites

- Python 3.10+
- For Salesforce: `simple-salesforce`
- For Google Sheets: Google Cloud service account credentials JSON
- For Slack: Slack Bot Token with `chat:write` scope
- For Excel: `openpyxl`, `xlsxwriter`
- For PDFs: `pdfplumber` or `PyMuPDF`

---

## License

MIT © Jeff Rotar | [jeffrotar@hotmail.com](mailto:jeffrotar@hotmail.com)

---

<div align="center">
  <sub>📍 Fargo, ND · Available for freelance automation and data engineering projects</sub>
</div>

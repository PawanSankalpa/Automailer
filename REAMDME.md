# Automate Mail Sender Project

A Python script that sends personalized emails automatically to a list of contacts on a scheduled interval using Gmail SMTP.

---

## Features

- Reads contacts from a CSV file (`contacts.csv`)
- Loads an email template with a placeholder for names (`[name]`)
- Sends customized emails to each contact
- Uses the `schedule` library to automate sending emails periodically
- Loads sensitive email credentials securely from a `.env` file

---

## Prerequisites

- Python 3.6+
- Gmail account with App Password enabled (recommended)
- Install dependencies:

```bash
pip install pandas schedule python-dotenv
```

## Setup Instructions

1. Clone or download this project.
2. Create a .env file in the project root with your Gmail credentials:

```env
EMAIL=your-email@gmail.com
PASSWORD=your-app-password
```
#### Important: **Use an App Password instead of your Gmail password for security.**

3. Prepare a contacts.csv file in the root folder with columns:

```csv
name,email
John Doe,john@example.com
Jane Smith,jane@example.com
```

4. Create an email template in ./templates/welcome_template.txt with [name] as the placeholder for personalization:

```txt
Hello [name],

Welcome to Automail!

Best regards,
Your Name
```
------------------------------------------------------------------------------------------------------------------------
# Usage
 - Run the script:
```bash
 python3 main.py
 ```
*By default, the script sends emails to all contacts every 10 seconds (for testing). To schedule daily emails at 9 AM, change the schedule line in main.py:*

```python
# schedule.every(10).seconds.do(send_to_all)
schedule.every().day.at("09:00").do(send_to_all)
```

# Stopping the Script
**Press Ctrl + C in the terminal to stop the script anytime.**

## Troubleshooting
- Avoid naming your script or any file schedule.py to prevent import conflicts.
- Make sure your .env credentials are correct.
- Check Gmail security settings to allow SMTP access.
- Verify internet connectivity if emails fail to send. 

## Author
***Pawan Sanklapa***







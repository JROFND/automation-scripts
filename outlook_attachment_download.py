
import os
import re
import win32com.client
import datetime
import pytz

def sanitize_filename(filename):
    """Remove invalid characters from filenames."""
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

def ensure_folder_exists(folder_path):
    """Create the folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def download_attachments_from_subfolder(subfolder_name, sender_email, save_folder, days_back=7, timezone="US/Central"):
    """Download attachments from a specific Outlook subfolder filtered by sender and date."""
    
    # Ensure save folder exists
    ensure_folder_exists(save_folder)

    # Set timezone and cutoff date
    tz = pytz.timezone(timezone)
    cutoff_date = tz.localize(datetime.datetime.now() - datetime.timedelta(days=days_back))

    # Connect to Outlook
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 = Inbox
    subfolder = inbox.Folders[subfolder_name]

    messages = subfolder.Items
    messages.Sort("[ReceivedTime]", True)

    # Loop through messages
    for message in messages:
        try:
            if message.Class == 43:  # MailItem
                if message.SenderEmailAddress.lower() == sender_email.lower():
                    received_time = tz.localize(message.ReceivedTime)
                    if received_time >= cutoff_date:
                        attachments = message.Attachments
                        for attachment in attachments:
                            safe_filename = sanitize_filename(attachment.FileName)
                            attachment.SaveAsFile(os.path.join(save_folder, safe_filename))
                        print(f"Downloaded from: {message.Subject}")
        except Exception as e:
            print(f"Error processing message: {e}")
            continue

# Configuration
save_folder = r"W:\"
target_sender = "GMB"
subfolder_name = "NAME"

# Run the function
download_attachments_from_subfolder(subfolder_name, target_sender, save_folder)

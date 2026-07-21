import os
import win32com.client
import datetime
import pytz  



# Template


def sanitize_filename(filename):
     """Remove invalid characters from filenames."""
     return re.sub(r'[\\/*?:"<>|]', "_", filename)

def download_attachments_from_subfolder(subfolder_name, sender_email, save_folder, days_back=7, timezone="US/Central"):
     """Download attachments from a specific Outlook subfolder filtered by sender and date."""
    # Ensure save folder exists


# Configuration
save_folder = r""
target_sender = ""

# Set timezone (e.g., Central Time)
central = pytz.timezone("US/Central")
cutoff_date = central.localize(datetime.datetime.now() - datetime.timedelta(days=7))

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 = Inbox
subfolder = inbox.Folders["Cardinal"]  # Replace with your actual subfolder name

messages = subfolder.Items
messages.Sort("[ReceivedTime]", True)

# Loop through messages
for message in messages:
    try:
        if message.Class == 43:  # MailItem
            if message.SenderEmailAddress.lower() == target_sender.lower():
                # Convert message.ReceivedTime to offset-aware
                received_time = message.ReceivedTime.replace(tzinfo=central)
                if received_time >= cutoff_date:
                    attachments = message.Attachments
                    for attachment in attachments:
                        attachment.SaveAsFile(os.path.join(save_folder, attachment.FileName))
                    print(f"Downloaded from: {message.Subject}")
    except AttributeError:
        continue



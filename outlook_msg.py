import win32com.client as client
import os
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()
# message.To="jesse.breidenbach@sanfordhealth.org"
# message.CC= "jeff.rotar@sanfordhealth.org"
# message.BCC = "jeff.rotar@sanfordhealth.org"
# message.Subject = "Happy Thursday"
# message.Body= "Wish you a happy thursday!"
# message.SentOnBehalfofName = "jeff_rotar@sanfordhealth.org"






# message.Save()
# message.Send()
# message.Delete()
import win32com.client as client
import os
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()


message.Save()
message.Send()
message.Delete()

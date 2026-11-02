from termcolor import colored as cd
import time
import smtplib
from email.message import EmailMessage
import os

# TOOL BANNER
os.system("clear")
def banner():
	_version_="1.0.0"
	return f'''
  ____  _____ _   _ ____  _____ ____
 / ___|| ____| \ | |  _ \| ____|  _ \ 
 \___ \|  _| |  \| | | | |  _| | |_) |
  ___) | |___| |\  | |_| | |___|  _ < 
 |____/|_____|_| \_|____/|_____|_| \_\   {_version_} 
		
	'''
tool_banner=banner()
print(cd(f"{tool_banner}", "magenta", attrs=['bold']))

# SENDER STARTING MSG.
print(cd("[*] SMS SENDER STARTING.", "yellow", attrs=['bold']))
time.sleep(.8)
print()

# INSTRUCTIONS TO USE THIS TOOL
print(cd("[!] INSTRUCTION TO USE.", "cyan", attrs=['bold']))
print(cd("[%] DEVELOPER : Khalid Saif.", "yellow", attrs=['bold']))
print()
print(cd('''
  1). OPEN EMAIL APP & ENABLE TWO FACTOR AUTHENTICATION.
  2). EMAIL > SECURITY > APP PASSWORD
  3). COPY PASSWORD WILL BE USE AHEAD

''', "grey", attrs=['bold']))

# CREATING CLASS OBJECT.
msg = EmailMessage()

# INPUTS INFORMATION.
APP_PASSWORD = input(cd("[?] ENTER APP PASSWORD : ", "green", attrs=['bold']))
subject = input(cd("[?] ENTER MAIL SUBJECT : ", "green", attrs=['bold']))
sender = input(cd("[?] ENTER SENDER GMAIL : ", "green", attrs=['bold']))
receiver = input(cd("[?] ENTER RECEIVER GMAIL : ", "green", attrs=['bold']))
print()
print(cd("[*] MASSAGE TO RECEIVER.", "grey", attrs=['bold']))
message_to_receiver = input(cd("[?] SEND MESSAGES TO RECEIVER : ", "yellow", attrs=['bold']))

# SENDER & RECEIVER EMAIL ADDRESS.
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

# MASSAGE FOR RECEIVER.
msg.set_content(message_to_receiver)

# BUILDING CONNECTION WITH SMTP.
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
	server.login(sender, APP_PASSWORD)
	server.send_message(msg)
	
# FIAL MSG.
print()	
print(cd(f"[@] EMAIL SENT TO {receiver}.", "magenta", attrs=['bold']))






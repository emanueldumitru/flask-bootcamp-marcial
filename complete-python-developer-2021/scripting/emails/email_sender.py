import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Emanuel Dumitru'
email['to']   = 'emanuel.dumitru9@gmail.com'
email['subject'] = 'You won 1000000 dollars'

email.set_content(html.substitute(name = 'TinTin'), html)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('emanuel.dumitru9@gmail.com','o parola')
    smtp.send_message(email)
    print('all good boss')

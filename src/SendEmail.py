import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(users: list):
    # get email and password from text file
    f = open('secretVars.txt', 'r')
    email = f.readline()
    password = f.readline()

    # establish connection and login
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)

    # makes message html supporting
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Daily Reminders"
    msg['From'] = "email"
    

    text = 'error'

    f = open("page.html", 'r')
    html = f.read()

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    part2.add_header('Content-Disposition', 'inline')

    msg.attach(part1)
    msg.attach(part2)

    # sends email to every user in users list
    for user in users:
        msg['To'] = user
        server.sendmail(email, user, msg.as_string())
    server.quit()

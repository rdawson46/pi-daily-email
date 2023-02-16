import smtplib

def send_email(users: list):

    f = open('secretVars.txt', 'r')
    email = f.readline()
    password = f.readline()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)

    msg = "hello"

    for i in users:
        server.sendmail(email, users[i], msg)
    server.quit()
    
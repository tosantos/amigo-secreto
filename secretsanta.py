import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace this with the email address you want to send emails from
sender_email = "<YOUR SENDER EMAIL GOES HERE>"

# Replace this with a generated App password from your Google Account
sender_password = "<YOUR APP PASSWORD GOES HERE>"

def send_secret_santa_email(sender, receiver, receiver_email):
    subject = "Amigo Secreto"
    body = f"Caro(a) {receiver},\n\nO teu amigo(a) secreto(a) é: {sender}!\n\nMelhores cumprimentos,\nO organizador do amigo secreto"

    # Create the MIMEText objects and encode them with UTF-8
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    msg['Subject'] = subject

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def assign_secret_santas(participants):
    santas = list(participants.keys())
    random.shuffle(santas)

    for i in range(len(santas)):
        sender = santas[i]
        receiver = santas[(i + 1) % len(santas)]
        receiver_email = participants[receiver]

        send_secret_santa_email(sender, receiver, receiver_email)


if __name__ == "__main__":
    participants = {
        "Name1": "name1@mail.com",
        "Name2": "name2@mail.com",
        "Name3": "name3@mail.com",
        "Name4": "name4@mail.com",
        "Name5": "name5@mail.com",
        "Name6": "name6@mail.com",
        "Name7": "name7@mail.com"
    }

    assign_secret_santas(participants)

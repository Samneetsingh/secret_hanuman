import random
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tabulate import tabulate
from pprint import pprint

GOOGLE_SERVER = {'host': 'smtp.gmail.com', 'port': 587}
LIVE_SERVER = {'host': 'smtp-mail.outlook.com', 'port': 587}
PEOPLE = { 'Mayank Chaudhary': {'email': 'Mayankc7991@gmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None},
           'Nancy Barman': {'email': 'Nams.nancy@gmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None},
           'Ramya Muthukumaran': {'email': 'frychip@gmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None},
           'Srishti Kumar': {'email': 'srishtikumar5@gmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None},
           'Debal Saha': {'email': 'z.chorghay@gmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None},
           'Zahraa Chorghay': {'email': 'sahadebal@gmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None},
           'Samneet Singh': {'email': 'samneetdhillon@hotmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None},
           'Vinod Mathews': {'email': 'vinodmathews@gmail.com', 'isSecretHanuman': None, 'hasSecretHanuman': None}
           }

def setSecretHanuman(person):
    availablePeople = [p for p in PEOPLE if ((PEOPLE[p]['isSecretHanuman'] is None) and p != person)]
    secretHanuman = availablePeople[random.randrange(len(availablePeople))]
    PEOPLE[person]['hasSecretHanuman'] = secretHanuman
    PEOPLE[secretHanuman]['isSecretHanuman'] = person

def sendEMail(subject, emailFrom, emailTo, message):
    msg = MIMEMultipart()
    msg['From'] = emailFrom
    msg['To'] = emailTo
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    server = smtplib.SMTP(GOOGLE_SERVER['host'], GOOGLE_SERVER['port'], "samneetd@gmail.com", timeout=120)
    server.ehlo()
    server.starttls()
    server.login("samneetd@gmail.com", "9811158933")
    server.sendmail(emailTo, emailFrom, msg.as_string())
    server.quit()

def main():
    subject = ""
    msg = """
    <p class="x_MsoNormal">Hello all,</p>
    <p class="x_MsoNormal">On this auspicious and holy occasion of my birthday and also Diwali, let us get together (like we do every other weekend), and celebrate in a manner we never have. This year, to things differently, we will wear our traditional clothes and then get intoxicated! To notch things up a bit, we will not be eating good food outside or ordering from outside, but we will take part in a potluck and suffer in each other&rsquo;s love!</p>
    <p class="x_MsoNormal">Another highlight of the evening will be a dance performance by Vinod and Nancy on Chaiyyan Chaiyyan!! Yayyyy!!!</p>
    <p class="x_MsoNormal">Also, as for the first time our secret group members will be together, we will have a secret hanuman event (and because I worked hard on writing a program for it while I was working from home!). So, this mail will have details of the person you will be buying gift for; buy a gift under $10 and make sure it&rsquo;s not something useful! I hope Debal does not get my name!</p>
    <p class="x_MsoNormal">So let us meet on 21<sup>st</sup>&nbsp;of October and celebrate this all-in-one event. As tradition goes let us all together wish that this Diwali,</p>
    <ul>
    <li class="x_gmail-MsoListParagraphCxSpFirst" dir="ltr"><strong>May Kaushik find friends and a group to be a part of</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpMiddle" dir="ltr"><strong>May Debal get a Kurta of his own size</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpMiddle" dir="ltr"><strong>May Nancy talks a bit more</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpMiddle" dir="ltr"><strong>May Vinod doesn&rsquo;t sleep on the night of celebration</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpMiddle" dir="ltr"><strong>May I don&rsquo;t get any more wisdom tooth</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpMiddle" dir="ltr"><strong>May Debal brings a gift for secret Hanuman</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpMiddle" dir="ltr"><strong>May Shristi stops hopping countries and settles down</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpMiddle" dir="ltr"><strong>May Ramya pay people and on time</strong></li>
    <li class="x_gmail-MsoListParagraphCxSpLast" dir="ltr"><strong>May Vinod doesn&rsquo;t sue anyone</strong></li>
    </ul>
    <p>And may we all stay together as a family away from our families and share our life together. Cheers!</p>
    <p><strong>FYI: I was kidding about the dance performance. It will be me again drunk and bruised!</strong></p>
    """
    for person, detail in PEOPLE.items():
        setSecretHanuman(person)
    pprint(PEOPLE)

    for person, detail in PEOPLE.items():
        try:
            sendEMail('Test Email', 'samneetd@gmail.com', 'samneetdhillon@hotmail.com', "This is the message!")
            #sendEMail(subject, 'samneetd@gmail.com', )
        except Exception as e:
            print(str(e))
            pass\


if __name__ == '__main__':
    main()



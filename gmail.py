import smtplib

_gmail_user = ... 
_gmail_password = ... 


def send_mail(message):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(_gmail_user, _gmail_password)
        message = 'Subject: {}\n\n{}'.format('vaccine sites', message) 
        server.sendmail(_gmail_user, _gmail_user, message) 
        server.quit()

    except Exception as e:
        print('error sending', e)

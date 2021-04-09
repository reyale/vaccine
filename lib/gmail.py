import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def render_html_table(title, data):
    res = "<p1>%s</p1>" % title
    res += '<table style="width:100%" border="1">'
    for d in data:
        res += "<tr><td>" + str(d) + "</td></tr>"

    res += "</table>"
    return res


def send_mail(sendemail, sendpassword, toemail, subject, html):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sendemail, sendpassword)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject 
    msg['From'] = sendemail 
    msg['To'] = toemail

    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

    server.sendmail(sendemail, toemail, msg.as_string())
    server.quit()

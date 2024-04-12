import smtplib

username = ""
password = ""


def send_mail(
    text="Email Body",
    subject="Hello world",
    from_email=username,
    to_emails=None,
):
    assert isinstance(to_emails, list)

    # login to my smptp server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()

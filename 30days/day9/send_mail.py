def send_mail(
    text="Email Body",
    subject="Hello world",
    to_emails=None,
):
    assert isinstance(to_emails, list)

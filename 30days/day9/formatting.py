msg_template = """Hello {name},
    Thank you for joining {website}. we are very happy to have you with us.
    """


def format_msg(my_name="noah", my_website="google.com"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg

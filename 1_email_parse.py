import re

RE_EMAIL = re.compile(r"^(\w+)@([a-zA-Z0-9\-]+\.[a-zA-Z]+)$")


def email_parse(email):
    if not RE_EMAIL.match(email):
        raise ValueError(f"wrong email: {email}")
    search = RE_EMAIL.search(email)
    return {
        "username": search.group(1),
        "domain": search.group(2)
    }


email_for_test = ["14@gmail.com"]

for email in email_for_test:
    try:
        email_dict = email_parse(email)
    except ValueError as e:
        print(email, " - ", e)
    else:
        print(email, " - ", email_dict)

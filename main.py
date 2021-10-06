
from src.email_fill import get_email_format, fill_emails


def main(names: list, example_email: str, example_name: str):
    contacts = fill_emails(
        names=names, email_format=get_email_format(example_email, example_name))
    return contacts

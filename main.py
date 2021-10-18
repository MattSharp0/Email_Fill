
import re


def get_email_format(email: str, name: str) -> dict:
    """
    Compares email against known list of possible formats, returing the format.
    Requires a known contact name and email. Returns a dict of the email data with domain, divider character (if present) and format.
    """

    # Check provided email is valid
    EMAIL_REGEX = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

    email = email.strip()
    if not re.search(EMAIL_REGEX, email):
        return

    # Split email
    # domain = (email.split('@'))[-1]
    email_split = email.split('@')
    username, domain = email_split[0], '@' + email_split[-1]

    # Split name
    full_name = name.split()
    name_length = len(full_name)
    if name_length > 2:
        middlename = ' '.join(
            [mn for mn in full_name[1: (name_length - 1)]])
    else:
        middlename = ' '

    firstname, lastname = full_name[0], full_name[-1]

    # check for divider character
    USERNAME_CHARS = r'[\'\.\-_!#\^~]'
    if re.search(USERNAME_CHARS, username):
        div = (re.findall(USERNAME_CHARS, username))[0]
    else:
        div = ''

    # Typical corporate email formats
    EMAIL_FORMATS = [{'email': {'div': div, 'domain': domain, 'order': {1: 'firstname', 2: 'div', 3: 'lastname', 4: '', 5: '', 6: 'domain'}}, 're_format': rf'{firstname}{div}{lastname}{domain}'},
                     {'email': {'div': div, 'domain': domain, 'order': {1: 'firstname', 2: 'lastname',
                                                                        3: '', 4: '', 5: '', 6: 'domain'}}, 're_format': rf'{firstname}{lastname}{domain}'},
                     {'email': {'div': div, 'domain': domain, 'order': {1: 'first_in', 2: 'lastname', 3: '',
                                                                        4: '', 5: '', 6: 'domain'}}, 're_format': rf'{(firstname[0])}{lastname}{domain}'},
                     {'email': {'div': div, 'domain': domain, 'order': {1: 'firstname', 2: '',
                                                                        3: '', 4: '', 5: '', 6: 'domain'}}, 're_format': rf'{firstname}{domain}'},
                     {'email': {'div': div, 'domain': domain, 'order': {1: 'firstname', 2: 'div', 3: 'middle_in', 4: 'div',
                                                                        5: 'lastname', 6: 'domain'}}, 're_format': rf'{firstname}{div}{(middlename[0])}{div}{lastname}{domain}'},
                     {'email': {'div': div, 'domain': domain, 'order': {1: 'first_in', 2: 'middle_in', 3: 'lastname',
                                                                        4: '', 5: '', 6: 'domain'}}, 're_format': rf'{(firstname[0])}{(middlename[0])}{lastname}{domain}'},
                     {'email': {'div': div, 'domain': domain, 'order': {1: 'first_in', 2: 'div', 3: 'lastname', 4: '', 5: '', 6: 'domain'}}, 're_format': rf'{(firstname[0])}{div}{lastname}{domain}'}]

    for format in EMAIL_FORMATS:
        re_format = format['re_format']
        if re.search(re_format, email, re.IGNORECASE):
            return format['email']


def fill_emails(contact_names: list, email_format: dict) -> list:
    """
    Takes a list of contact names (first and last) and an email format. 
    Returns a list of contacts as dicts with firstname, lastname and email.
    """
    contacts = []

    # split names
    for name in contact_names:
        full_name = name.split()
        name_length = len(full_name)
        if name_length > 2:
            middlename = ' '.join(
                [mn for mn in full_name[1: (name_length - 1)]])
            middle_in = middlename[0]
        else:
            middlename = ''
            middle_in = ''

        firstname, lastname = full_name[0], full_name[-1]

        # dict for email filling
        name_parts = {'firstname': firstname,
                      'first_in': firstname[0], 'middle_in': middle_in, 'lastname': lastname, 'div': email_format['div'], 'domain': email_format['domain']}

        eli = []
        for v in email_format['order'].values():
            if v:
                eli.append(name_parts[v])
        email = ''.join(eli)

        contact = {'first_name': (
            firstname + ' ' + middlename), 'last_name': lastname, 'email': email.lower()}

        contacts.append(contact)
    return contacts


def main(names: list, example_email: str, example_name: str):

    email_format = get_email_format(example_email, example_name)

    if email_format:
        contacts = fill_emails(contact_names=names, email_format=email_format)
        return contacts
    else:
        return

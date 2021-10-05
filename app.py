import re


def get_email_format(email: str, name: str):

    # Check provided email is valid
    EMAIL_REGEX = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

    email = email.strip()
    if not re.search(EMAIL_REGEX, email):
        print(f'Provided email ({email}) is not valid')
        return 'Bad email'

    # Split email
    # domain = (email.split('@'))[-1]
    email_split = email.split('@')
    username, domain = email_split[0], email_split[-1]

    # Split name
    full_name = name.split()
    name_length = len(full_name)
    if name_length > 2:
        middlename = ' '.join(
            [mn for mn in full_name[1: (name_length - 1)]])
    else:
        middlename = ' '

    firstname, lastname = full_name[0], full_name[-1]

    # check for seperator character
    USERNAME_CHARS = r'[\'\.\-_!#\^~]'
    if re.search(USERNAME_CHARS, username):
        sep_char = (re.findall(USERNAME_CHARS, username))[0]
    else:
        sep_char = ''

    # Typical corporate email formats [\._\-]
    EMAIL_FORMATS = {f'first{sep_char}last@domain': rf'{firstname}{sep_char}{lastname}@{domain}',
                     f'first{sep_char}mi{sep_char}last@domain': rf'{firstname}{sep_char}{(middlename[0])}{sep_char}{lastname}@{domain}',
                     'firstlast@domain': rf'{firstname}{lastname}@{domain}',
                     'filast@domain': rf'{(firstname[0])}{lastname}@{domain}',
                     'first@domain': rf'{firstname}@{domain}'}

    # Check provided email against known formats
    for format, format_string in EMAIL_FORMATS.items():
        if re.search(format_string, email, re.IGNORECASE):
            return format


test_emails = [('msharp@telesign.com', 'Matthew Benjamin Sharp'), ('haleyhaltom@gmail.com', 'Haley Ann Haltom'),
               ('John_smith@smith.com', 'John Smith'), ('wilbur.hammond@gmail.com', 'Wilbur Hammond'), ('mark@hotmail.com', 'Mark Johnson')]

for email, name in test_emails:
    format = get_email_format(email, name)
    print(f'Email format for {name} is {format}')

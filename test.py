from src.email_fill import get_email_format, fill_emails

test_emails = [('msharp@telesign.com', 'Matthew Benjamin Sharp'), ('haleyhaltom@gmail.com', 'Haley Ann Haltom'),
               ('John_smith@smith.com', 'John Smith'), ('wilbur.hammond@gmail.com', 'Wilbur Hammond'), ('mark@hotmail.com', 'Mark Johnson'), ('michael#outlook.com', 'Michael Jordan')]


# email_format = get_email_format('matthew.sharp@gmail.com', 'Matthew Sharp')
# email_format = get_email_format('msharp@gmail.com', 'Matthew Sharp')
email_format = get_email_format('mbsharp@gmail.com', 'Matthew Benjamin Sharp')

test_names = ['Haley Ann Haltom', 'Jimothy Bobert',
              'John Smith', 'Matthew Sharp']

contacts = fill_emails(test_names, email_format)

print(contacts)

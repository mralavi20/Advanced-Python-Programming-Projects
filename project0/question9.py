import re

email = str (input ())
email_format = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

if (re.fullmatch (email_format, email)):
    print ("OK")
else:
    print ("WRONG")
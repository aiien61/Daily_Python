#! usr/bin/env python3
import re, pyperclip

# url = 'https://automatetheboringstuff.com/files/examplePhoneEmailDirectory.pdf'

# Create a regrex for phone numbers
# e.g. 415-555-0000, 555-0000, (415)555-0000, 555-0000 ext 12345, ext. 12345, x12345
phone_regrex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code (optional)
(\s|-|\.)?                       # separator
(\d{3})                         # first 3 digits
(\s|-|\.)                       # separator
(\d{4})                         # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (optional)
)''', re.VERBOSE)

# Create a regrex for email addresses
email_regrex = re.compile(r'''(
[\w.+%\-]+   # name part
@            # symbol
[\w.+%\-]+   # domain part
)''', re.VERBOSE | re.IGNORECASE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email addresses / phone numbers from the text
extracted_phone_numbers = phone_regrex.findall(text)
extracted_emails = email_regrex.findall(text)

# Copy the extracted email/phone to the clipboard
if extracted_phone_numbers is None and extracted_emails is None:
    print('No phone numbers or email addresses found.')
else:
    matches = [phone_number[0] for phone_number in extracted_phone_numbers]
    matches.extend(extracted_emails)
    result = '\n'.join(matches)

pyperclip.copy(result)

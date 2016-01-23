#! python3

import re,pyperclip

# Create regex for amounts
amountRegex = re.compile(r'''
\$
(\d+,?\d+,?\d+)     # The digits
.?\d+               # The decimals
''', re.VERBOSE)

# Create regex for e-mail addresses
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+    # name part
@   # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# Get the text of the clipboard
text = pyperclip.paste()

# Extract e-mails and amounts
extractedAmount = amountRegex.findall(text)
extractedEmail = emailRegex.findall(text)

mergedList = [list(l) for l in zip(extractedEmail, extractedAmount)] # create a merged list (email + amount)
list = [';'.join([str(c) for c in lst]) for lst in mergedList] # un-nest the list
results = '\n'.join(list) # create a string from the list

#  Copy the extracted text to clipboard
pyperclip.copy(results) # copy the results to clipboard

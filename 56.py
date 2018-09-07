import re
a=input("")
print(bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', a)))



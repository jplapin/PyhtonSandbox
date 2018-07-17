

import re

string = "'I'M NOT YELLING', she said. Though we knew she was."

#removes all Capital letters
new = re.sub('[A-Z]','',string)
print(new)

#removes all small letters
new = re.sub('[a-z]','',string)
print(new)

#removes all punctuation
new = re.sub('[.,\']','',string)
print(new)

#removes everything
new = re.sub('[.,\'a-zA-Z]','',string)
print(new)

#removes capital letters, punctuation and spaces 
new = re.sub('[.,\'A-Z+" "]','',string)
print(new)

string2 = "'I'M NOT YELLING', she said. Though we knew she was. 6 - 5 +54.6"
#removes everything except numbers 
new2 = re.sub('[^0-9]','',string2)
print(new2)

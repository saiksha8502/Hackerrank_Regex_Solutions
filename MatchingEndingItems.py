Regex_Pattern = r'^[A-Za-z]*s$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
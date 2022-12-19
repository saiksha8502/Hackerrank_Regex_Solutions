Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"	# Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

from typing import List
import re
def isEmail(email: str) -> bool:
    # write your code here ^_^
    search = re.search(r'^([A-z]([0-9(-_)]|w+)|\w+)(@{1})+([a-z]{1,})(\.)([a-z]{2,})$',email)
    return True if type(search) == re.Match else False
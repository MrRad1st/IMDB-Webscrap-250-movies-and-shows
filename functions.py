import re

def extract_info(pattern, text):
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return "Not found"
        
def space_between_words(text):
    lst = list(text)
    for i in range(len(lst)):
        if lst[i].isupper():
            if i!=0 and lst[i-1] != " ":
                lst[i] = ","+lst[i]
    s = ""
    for item in lst:
        s = s+item
    return s
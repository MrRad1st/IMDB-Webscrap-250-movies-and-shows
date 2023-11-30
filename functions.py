def clear_spaces_before_string(s):
    if s == None or len(s) == 0:
        return
    i = 0
    while s[i] == ' ' and i < len(s):
        s = s[i+1:]
        i+=1
    if s[0] == ' ':
        s = s[1:]
    return s

def clear_after_comma_spaces(s):
    if s == None or len(s) == 0:
        return
    while s != s.replace(', ',','):
        s = s.replace(', ',',')
    return s

def make_info_ready(s):
    return remove_excess_newlines(clear_after_comma_spaces(clear_spaces_before_string(s)))

def remove_excess_newlines(s):
    if s == None or len(s) == 0:
        return
    while s != s.replace('\n ','\n'):
        s = s.replace('\n ','\n')
    while s != s.replace('\n\n','\n'):
        s = s.replace('\n\n','\n')
    while s[-1] == '\n':
        s = s[:-1]
    return s

def remove_space_at_the_end(s):
    if s[-1] == ' ':
        return s[:-1]
    else:
        return s

def remove_newline_at_the_end(s):
    if s[-1] == '\n':
        return s[:-1]
    else:
        return s


def cut_string_in_half(s):
    midpoint = len(s) // 2
    first_half = s[:midpoint]
    second_half = s[midpoint:]
    return first_half


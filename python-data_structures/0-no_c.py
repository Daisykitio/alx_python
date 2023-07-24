

def no_c(my_string):
    result = []
    for char in my_string:
        if char not in ['c', 'C']:
            result.append(char)
new_string = ''.join(result)
    return new_string

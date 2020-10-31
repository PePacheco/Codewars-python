
# First non-repeating character

def first_non_repeating_letter(string):
    stringLower = string.lower()
    for key, letter in enumerate(stringLower):
        if(stringLower.count(letter) == 1):
            return string[key]
    return ''
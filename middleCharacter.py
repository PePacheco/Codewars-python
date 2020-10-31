import math

# Get the Middle Character

def get_middle(s):
    if(len(s) % 2 == 0):
        firstIndex = int((len(s)/2)-1)
        secondIndex = int(len(s)/2)
        return s[firstIndex] + s[secondIndex]
    else:
        return s[math.floor(len(s)/2)]
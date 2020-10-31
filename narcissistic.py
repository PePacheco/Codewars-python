
# Does my number look big in this?

def narcissistic( value ):
    total = 0
    for index,data in enumerate(str(value)):
        total += int(data)**(len(str(value)))
    if(total == value):
        return True
    else:
        return False
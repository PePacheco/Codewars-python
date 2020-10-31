def rot13(message):
    answer = []
    for letter in message:
        if(letter.isalpha()):
            code = ord(letter) + 13
            if(letter.isupper()):
                if(code > 90):
                    code = (code - 90) + 64    
                answer.append(chr(code))
            else:
                if(code > 122):
                    code = (code - 122) + 96   
                answer.append(chr(code))
        else:
            answer.append(letter)
    return ''.join(answer)
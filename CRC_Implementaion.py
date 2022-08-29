def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2division(Bstring, gstring):
    end = len(gstring)
    tmp = Bstring[0 : end]
    while end < len(Bstring):
        if tmp[0] == '1':
            tmp = xor(gstring, tmp) + Bstring[end]
        else:
            tmp = xor('0'*end, tmp) + Bstring[end]
        end += 1
    if tmp[0] == '1':
        tmp = xor(gstring, tmp)
    else:
        tmp = xor('0'*end, tmp)
    remainder = tmp
    return remainder

def addition(Mstring,remainder):
    Mstring=Mstring[::-1]
    remainder=remainder[::-1]
    Tstring=''
    i=0
    for i in range(len(remainder)):
        if remainder[i]==Mstring[i]:
            Tstring+='0'
        else:
            Tstring+='1'
    Tstring+=Mstring[i:]
    Tstring=Tstring[::-1]
    return Tstring

bstring=input('Enter the message bit string: ')
gstring=input('Enter the generator bit string: ')
len_bstring=len(bstring)
len_gstring=len(gstring)
GP_degree=len_gstring-1
Mstring=bstring+('0'*GP_degree)
print(GP_degree)
print(Mstring)
remainder=mod2division(Mstring, gstring)
print('Error in Transmission:',remainder)
Tstring=addition(Mstring,remainder)
print('Corrected Transmission:',Tstring)



#Parity Generator
def evenbitparitygen(msg):
    paritybit='0'
    bitcount=msg.count('1')
    if bitcount%2==1:
        paritybit='1'
    msg+=paritybit
    return msg

def oddbitparitygen(msg):
    paritybit='0'
    bitcount=msg.count('1')
    if bitcount%2==0:
        paritybit='1'
    msg+=paritybit
    return msg

#Parity Check
def evenbitparitycheck(msg):
    parityerror='0'
    bitcount=msg.count('1')
    if bitcount%2==1:
        parityerror='1'
    return parityerror,msg

def oddbitparitycheck(msg):
    parityerror='0'
    bitcount=msg.count('1')
    if bitcount%2==0:
        parityerror='1'
    return parityerror,msg
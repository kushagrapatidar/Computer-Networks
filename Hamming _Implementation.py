#[0,1,2,3,4,5,6]
#[7,6,5,4,3,2,1]
def sender(sbits):
    mpos=[0,1,2,4]
    rpos=[3,5,6]
    tmessage=[0]*7
    sbits=list(map(int,sbits))
    i=0
    for pos in mpos:
        tmessage[pos]=sbits[i]
        i+=1
    bitset=[0]*3
    bitset[0]=[0,1,2]
    bitset[1]=[0,1,4]
    bitset[2]=[0,2,4]
    pos=0
    for _ in range(len(bitset)):
        for i in bitset[_]:
            tmessage[rpos[pos]]^=tmessage[i]
        pos+=1
    return tmessage

def reciever(rbits):
    def todec(error):
        dec=0
        i=0
        while error>0:
            dec+=(2**i)*(error%10)
            error//=10
            i+=1
        error=dec
        return error

    bitset=[0]*3
    bitset[0]=[0,2,4,6]
    bitset[1]=[1,2,5,6]
    bitset[2]=[3,4,5,6]
    rbits=list(map(int,rbits))
    rbits=rbits[::-1]
    print(rbits)
    error=''
    for _ in range(len(bitset)):
        xor=0
        for i in bitset[_]:
            xor^=rbits[i]
        error=str(xor)+error
    error=todec(int(error))
    if error==0:
        print(f'No Error Found')
    else:
        print(f'Error bit index: {error}')

sbits=input('Enter the 4 bit message string: ')
tmessage=sender(sbits)
message=''
for i in tmessage:
    message+=str(i)
print('Transmitted Message:',message)
message=input('Enter the recieved message bit string: ')
reciever(message)
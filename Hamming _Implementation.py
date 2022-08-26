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
bitset[2]=[3,2,5,6]
sbit=input('Enter the sender bit string: ')
rbit=list(map(int,input('Enter the reciever bit string: ')))
rbit=rbit[::-1]
error=''
for _ in range(len(bitset)):
    xor=0
    for i in bitset[_]:
        xor^=rbit[i]
    error=str(xor)+error
error=todec(int(error))
print(f'Error bit index: {error}')
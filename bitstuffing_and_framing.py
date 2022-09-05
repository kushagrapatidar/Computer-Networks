def bitstuffing(msg,key,string):
    while string in msg:
        msg=msg.replace(string,key)
    return msg

def frame(msg,frames,flag):
    string='1'*flag.count('1')
    key=string[:-1]+'01'
    tempmsg=flag
    for _ in frames:
        tempmsg+=bitstuffing(msg[:_],key,string)
        tempmsg+=flag*2
        msg=msg[_:]
    msg=tempmsg[:-len(flag)]
    return msg

msg=input('Enter the bit message: ')
frames=list(map(int,input('Enter the frame sizes: ').split()))
flag=input('Enter the flag pattern: ')
msg=frame(msg,frames,flag)
print(msg)
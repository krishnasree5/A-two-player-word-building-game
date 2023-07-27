players=['Player1','Player2']
print("Player1:",end="")
word=input()
c=1
while True:
    print(players[c],":",end='')
    if c==0:
        c=1
    else:
        c=0
    last=word[-1]
    word=input()
    first=word[0]
    if first==last:
        pass
    else:
        print(players[c],"won")
        break

        
    
    

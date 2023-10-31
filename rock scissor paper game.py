import random
def play(match):
    i=0
    p=0
    c=0
    while (i<match):   
        n=input("choose:'r' for rock,'s' for scisors,'p' for paper: ")
        a=random.choice(['r','p','s'])
            
        if a==n:
            print("its a tie")
        # r>s s>p p>r
        elif (n=='r' and a=='s')or (n=='s'and a=='p') or (n=='p' and a=='r'):
            print("you won:)!!!")
            p+=1
        else:   
            print("you Lose :(")
            c+=1
        i+=1
    if p==c:
        print(f'its a tie!! your score:{p};computer score:{c}')
    elif p>c:
        print(f'you won!! your score:{p};computer score:{c}')
    else:
        print(f'you lose!! your score:{p};computer score:{c}')
match=int(input("Enter no matches:"))
play(match)

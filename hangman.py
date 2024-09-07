import random
words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
c=random.choice(words)
d=len(c)
qpf=d+3
ff=[]
for i in range(0,d):
    ff.append("_")
e=list(c)
ee=list(c)
qpp="".join(e)
qppp="".join(ff)
print(f"{qppp}")
f=True
ss=d+3
while f :
    print(f"Your word is {d} lettered word and you have only {ss+3} guesses left")
    g=input("Guess a character : (Enter stop to quit the program)")
    if ss==0:
            f=False
            print(f"The word was {c} . You lost!!!(Due to usage of all guesses)")
    elif g in e :
        for i in range(0,d):
            hh=e[i]
            if hh==g:
                ff[i]=g
        print("".join(ff))
        ss=ss-1
        if ee==ff:
            print(f"You have guessed the word {c}.It took {qpf-ss} guesses.")
            f=False
    elif g=="stop":
        print(f"You have stopped the program.The word was {c}")
        f=False
    else :
        print("The character is not there in a word guess again.")
        ss=ss-1
        pass

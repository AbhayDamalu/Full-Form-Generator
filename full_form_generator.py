print("               F U L L   F O R M   G E N E R A T O R  [v1.0]")
print()

def random_meaning(data,alphabet):
    import random
    nominee=[]
    for word in data:
        if word[0].lower()==alphabet.lower():
            nominee+=[word[:-1]]
    return random.choice(nominee)

def display(name,alpha_meaning):
    
    for (alpha,meaning) in alpha_meaning:
        print("---------------------")
        if (alpha,meaning)==(None,None):
            print()   
        else:
            print(alpha,":",meaning)
    print("---------------------")
    print()
    print(name.capitalize(),"means -->")
    print("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((")
    for (alpha,meaning) in alpha_meaning:
        if (alpha,meaning)==(None,None):
            print()
        else:
            print(meaning.capitalize(),end="  ")
    print()
    print(")))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))")
    print()
    
alpha_meaning_pair=[]


while True:
    
    name=input("Enter name : ")
    print()
    while True:
        file=open("personality.txt","r")
        data=file.readlines()
        file.close()
        lower_data=[i.lower() for i in data]
        data=list(set(lower_data))
        alpha_meaning_pair=[]
        for Word in name.split():
            for alphabet in Word:
                meaning=random_meaning(data,alphabet)
                alpha_meaning_pair+=[(alphabet.upper(),meaning.lower())]
                data.remove(meaning+"\n")     # avoid repetition
            alpha_meaning_pair+=[(None,None)]
        del (alpha_meaning_pair[-1])
        display(name,alpha_meaning_pair)
        print("Enter (O) to re-generate or (X) to abort")
        ch=input(">>>")
        while ch.lower() not in ["o","x"]:
            print("Invalid choice...Enter again !!")
            ch=input(">>>")
        if ch.lower()=="x":
            break
    print()    

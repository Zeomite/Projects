word= list("Beekeeper".lower())
guessed=[]
string=""
count=0
while count<=7:
    inp= input("Enter letter: ")
    if inp.lower() in word:
        guessed.append(inp)
    else:
        count+=1
    for i in word:
        if i in guessed:
            string+=i
        else:
            string+="_"
    if not "_" in string:
        print("You win!")   
        break 
    if count==7:
        print("You Lose!")

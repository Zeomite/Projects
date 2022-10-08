word= list("Beekeeper".lower())
guessed=[]
string="_ _ _ _ _ _ _ _ _"
count=0
print(string)
while count<=7:
    inp= input("Enter letter: ").lower()
    if inp in word and inp not in guessed:
        guessed.append(inp)
    else:
        count+=1
    string=""
    for i in word:
        if i in guessed:
            string+=i
        else:
            string+=" _"
    print(string)
    if not "_" in string:
        print("You win!")   
        break 
    if count==7:
        print("You Lose!")
        break

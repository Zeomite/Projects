print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stages.reverse()
import random
from hangman_words import word_list
word= random.choice(word_list).lower()
guessed=[]
string="_"*len(word)
count=0
print(string)
while count<=6:
    print(stages[count])
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
    if count==6:
        print(stages[count])
        print("You Lose!")
        break
print(f"The word was {word}.")
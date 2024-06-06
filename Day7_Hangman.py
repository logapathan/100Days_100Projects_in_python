import random
file=open("words.txt","r")
data=file.read()
word_list=data.split('\n')
file.close()
random_word=random.choice(word_list).lower()

display=[]


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


print(logo)
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

for i in range(0,len(random_word)):
    display.append("_")
print(stages[-1])
lives=6

while "_" in display:
    
    print(*display,sep=" ")

    guess_letter=input("Guess a letter:").lower()
    
    life=0
    if guess_letter in display:
            print("You have already guessed the letter")
    for i in range(0,len(random_word)):
        
        if random_word[i]==guess_letter:
            display[i]=guess_letter
            life=1

    if life==0:
        lives-=1
        print(f"You guessed the letter '{guess_letter}', which is not in the word. You lose a life")
        print(*display,sep=" ")
        print(stages[lives])    
    
    if lives<=0:
        print("Game Over. Hangman Died")
        print(f"The correct word is {random_word}")
        break
    
if lives>0:
    print(*display,sep=" ")
    print(f"You Won!!!.")





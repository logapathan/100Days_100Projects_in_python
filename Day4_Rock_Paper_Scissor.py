rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors")
user=int(input())
computer=random.randint(0,2)
if user==computer:
    if user==0:
        print(f"You: \n {rock} \nComputer: \n {rock} \n It's a Draw")
    elif user==1:
        print(f"You: \n {paper} \nComputer: \n {paper} \n It's a Draw")    
    elif user==2:
        print(f"You: \n {scissors} \nComputer: \n {scissors} \n It's a Draw")
elif user==0 and computer==1:
    print(f"You: \n {rock} \nComputer: \n {paper} \n Computer Wins.")
elif user==0 and computer==2:
    print(f"You: \n {rock} \nComputer: \n {scissors} \n You: Win.")     
elif user==1 and computer==0:
    print(f"You: \n {paper} \nComputer: \n {rock} \n You: Win.")       
elif user==1 and computer==2:
    print(f"You: \n {paper} \nComputer: \n {scissors} \n Computer Wins.")
elif user==2 and computer==0:
    print(f"You: \n {scissors} \nComputer: \n {rock} \n Computer Wins.")
elif user==2 and computer==1:
    print(f"You: \n {scissors} \nComputer: \n {paper} \n You: win.")
else:
    print("invalid input.")
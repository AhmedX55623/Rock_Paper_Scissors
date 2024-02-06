import random

draws = [
'''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''
,
'''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''
,
''' 
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  ]
rules = """
******* Rules ********

1) rock beat scissors
2) scissors beat paper
3) paper beat rock
"""
rps = ['Rock','Paper','Scissors']
print(f"welcome to {rps[0]}, {rps[1]}, {rps[2]} game\n")
help = input("press 'enter' to continue or type (Help) for the rules  ").capitalize()
computer_choice = random.choice(rps)

user_choice_up = None
com_choice_up = None

if help == "Help":
	print(rules)	
elif not help:
	pass
else:
	print("invaild")

user_choice = input(f"plese enter your choice [{rps[0]}], [{rps[1]}], [{rps[2]}]: ").capitalize()

if computer_choice == rps[0]:
	com_choice_up = draws[0]
elif computer_choice == rps[1]:
	com_choice_up = draws[1]
elif computer_choice == rps[2]:
	com_choice_up = draws[2]

if user_choice == rps[0]:
	user_choice_up = draws[0]
elif user_choice == rps[1]:
	user_choice_up = draws[1]
elif user_choice == rps[2]:
	user_choice_up = draws[2]

#rules
if(
   (user_choice == rps[0] and computer_choice == rps[2])
or (user_choice == rps[2] and computer_choice == rps[1]) 
or (user_choice == rps[1] and computer_choice == rps[2])
):
	print(f"user wins\nuser choice:\n{user_choice_up}\ncomputer choice {com_choice_up}\n{user_choice} beats {computer_choice}")
elif user_choice == computer_choice:
	print(f"user draws\nuser choice:\n{user_choice_up}\ncomputer choice {com_choice_up}")
elif user_choice not in rps:
	print("\ninvalid choice")
else:
	print(f"user lose\nuser choice:\n{user_choice_up}\ncomputer choice {com_choice_up}")

input()	

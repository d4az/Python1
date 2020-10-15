#importing random repo first
import random 
  
print("The Rules Of this game are follows : \n\n"
                                +"Rock vs pape => paper wins \n"
                                + "Rock vs scissor => Rock wins \n"
                                +"paper vs scissor =>scissor wins \n") 

print("Good Luck!\n")
  
while True: 
    print("Enter Your Choice :\n")
    print("1 --> Rock")
    print("2 --> Paper")
    print("3 --> Scissor\n")
      


    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
          
  
    print("You choose --> " + choice_name) 
    print("\nNow just let computer to select.../\n") 
  

    comp_choice = random.randint(1, 3) 
   

    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 
 
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("ohh Computer chooose : " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  

    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("paper wins! => ", end = "") 
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("Rock wins! =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins! =>", end = "") 
        result = "scissor"
  
    if result == choice_name: 
        print("<== Ohh You Won!==>") 
    else: 
        print("<== Computer wins! ==>") 
          
    print("Hey Lets just try again! (y/n)") 
    ans = input() 
  
    if ans == 'n' or ans == 'N': 
        break
      
print("\nTHANKYOU FOR PLAYING :D") 


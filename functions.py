import replit

def startup():
  while True:
    start = input("Do you want to play the game? ").strip().capitalize()
    if start == "Y" or start == "Yes":
      print("Ok, lets play then\n")
      input("Press ENTER TO CONTINUE")
      replit.clear()
      break
    elif start == "N" or start == "No":
      print("Ok, just run the program if you want to play again")
      quit()

def name():
  while True:
    name.name = input("Now before we begin, how about I know your name? ").strip().capitalize()
    if name.name != "":
      if name.name == "Taylan":
        print(name.name + "... What an excellent name! Now lets begin properly.\n")
        input("Press ENTER TO CONTINUE")
      else:
        print(name.name + "... What a name. Now lets begin properly.\n")
        input("Press ENTER TO CONTINUE")
      break
    else:
      print("Follow the instructions... or else...")

def decision1():
  count = 0
  
  while True:
    replit.clear()
    decision = input("Do you want to:\n a) Climb the wall\n b) Go around the fence\n c) Go around the block to the house\n").lower()
    
    if decision == "a":
      print("You tried to climb the wall, but slipped and fell off\n")
      input("Press ENTER TO CONTINUE")
      count += 1
    elif decision == "b":
      print("You tried to go around the fence, but realised you are in a garden... surrounded by a fence... You lost 20 iq points\n")
      input("Press ENTER TO CONTINUE")
      count += 1
    elif decision == "c":
      print("You ran round the block, only to realise it went into the house next to yours... You lost 20 stamina and iq points.\n")
      input("Press ENTER TO CONTINUE")
      count += 1
    else:
      print("Enter a, b, or c to make your decision. Please just make my life easier so that I dont have to add extra lines of code.\n")
    if count == 3:
      break

def decision1con():
  print("Ok, maybe I was a bit too harsh on you, so I'll give you another option...\n")
  while True:
    decision = input("d) Retrieve ball\n")
    replit.clear()
    if decision != "d":
      print("You had 1 job... 1 JOB... TO PRESS THE LETTER D AND ENTER!!!! HOW COULD YOU MESS THAT UP!!!! Huff... Just... try again.")
    elif decision == "d":
      print("Good. Now let's continue with the story...")
      input("Press ENTER TO CONTINUE")
      break

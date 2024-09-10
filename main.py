from functions import startup, name, decision1, decision1con
import replit

startup()
print("Welcome to my little game I'm trying to develop.\nIt's lovely to see you here.")
input("Press ENTER TO CONTINUE")

replit.clear()
name()
replit.clear()

print("You, a lonely person wanders into a garden and starts to play football.\n"
     "10 minutes later... Oh no! You kicked the ball over! Come on", name.name, "let's go get the ball!")
input("Press ENTER TO CONTINUE")
replit.clear()
 
decision1()
replit.clear()
decision1con()
replit.clear()

input("Decision d, ah yes, the almighty option...\n You decided to jump onto the bins to get over the fence. You did it! Without hurting yourself too.")

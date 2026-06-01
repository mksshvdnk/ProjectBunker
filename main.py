import typer
import bunkerLogic as bunker
import subprocess
import time



app = typer.Typer()

running = True
AIOn = False
pg = bunker.PlayerCardGenerator()


#Tries to initialize AI
def initAI():
   global AIOn
   if AIOn == False:
     try:
      subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
      time.sleep(2)
      AIOn = True
     except FileNotFoundError:
      print("AI Model in not installed")

#generates a random Playercard
def generateNewAIGame():
    global AIOn
    initAI()

    if AIOn:
     print("Generating new game...")
     pg.generateNewAIGame()
     print("Your game is generated. You can create your players")

#Generates values for a parameter in AI and restarts the game
def addAIParameter():
   global AIOn
   initAI()

   if AIOn:
    command = input("What is the name of the parameter?\n")
    print("Generating new parameter...")
    if pg.addAIParameter(command):
     print("New parameter is generated. Restarting the game.\n")
     deleteAllPlayers()

#generates a random Playercard
def generateRandomPlayer():
   pg.generateRandomPlayer()
   pg.players[-1].writePars()

def generateRandomPlayers():
   try:
      command = int(input("How many players do you want to generate?\n"))
      if command > 0:
       for i in range(command):
        generateRandomPlayer()
        print("\n--------\n")
   except ValueError:
      print("Please enter a valid number.\n")

def deletePlayer():
    try:
        index = int(input("Enter player index to delete:\n"))
        pg.deletePlayer(index)
        print(f"Player {index} deleted.")
    except ValueError:
        print("Please enter a valid number.\n")

def deleteParameter():
    parameter = input("Enter parameter to delete:\n")
    pg.deleteParameter(parameter)

def deleteAllPlayers():
    pg.deleteAllPlayers()
    print("All players deleted.")

#Gives all commands
def help():
   print("all commands are\n")
   print("\n".join(commands.keys()))

#Closes the programm
def quit():
    global running
    running = False

#List of commands
commands = {
    "generateNewAIGame": generateNewAIGame,
    "addAIParameter": addAIParameter,
    "generatePlayer": generateRandomPlayer,
    "generateManyPlayers": generateRandomPlayers,
    "deletePlayer": deletePlayer,
    "deleteAllPlayers": deleteAllPlayers,
    "deleteParameter": deleteParameter,
    "quit": quit,
    "help": help
}

#Called in the CL. Manages user input 
@app.command()
def start():
    global running 
    while running:
        command = input("What can I do for you?\nType 'help' for a list of commands.\n\n")    
        if command in commands:
            print("\n----------------------")
            commands[command]()
            print("\n----------------------")
        else:
         print("Unknown command. Type 'help' for a list of commands.")


if(__name__ == "__main__"):
    app()
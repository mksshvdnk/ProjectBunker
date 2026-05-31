import typer
import bunkerLogic as bunker

app = typer.Typer()

running = True
pg = bunker.PlayerCardGenerator()


#generates a random Playercard
def generateRandomPlayer():
   pg.generateRandomPlayer()
   pg.players[-1].writePars()

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
  "generateRandomPlayer": generateRandomPlayer,
  "quit" : quit,
  "help" :  help

}

#Called in the CL. Manages user input 
@app.command()
def start():
    global running 
    while running:
        command = input("What can I do for you?\nType 'help' for a list of commands.\n")    
        if command in commands:
            print("\n----------------------")
            commands[command]()
            print("\n----------------------")
        else:
         print("Unknown command. Type 'help' for a list of commands.")


if(__name__ == "__main__"):
    app()
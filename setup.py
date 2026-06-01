import subprocess
import sys

print("Installing dependencies...")
subprocess.run([sys.executable, "-m", "pip", "install", "typer", "requests"])



while True:
 AiDownload =  input("Do you want to install the AI model(2,2 GB) for additional functions? Yes/No")
 if AiDownload == "Yes":
    print("Downloading AI model...")
    subprocess.run(["ollama", "pull", "llama3.2:3b"])
    break
 elif AiDownload == "No":
    print("Running programm without AI functions")
    break
 else:
    print("The input is incorrect. Type Yes/No")

print("Setup complete. Run 'py main.py start' to start the program.")
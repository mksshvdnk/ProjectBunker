from pathlib import Path
import random
import requests as rq



#A card of a player
class Playercard:
    def __init__(self,index, **kwargs):
        self.index = index
        self.parameters = kwargs
        
#Gives player's parameters in a console
    def writePars(self):
     if self.parameters:
        print(f"Player {self.index}")
        print("\n".join(f"{key} : {value}" for key, value in self.parameters.items()))


#Generates player card based on given data  
class PlayerCardGenerator:
    def __init__(self):

        #list of all Players
        self.players : list[Playercard] = []
        
        #basic parameters
        self.basicParameters = ["Age", "Gender", "Skill", "Weakness"]

        #File with parameters
        self.parametersPath = next(Path.cwd().rglob("Parameters.txt"),None)
        
        #List of parameters
        self.parameters = self.basicParameters.copy()

        #Clusters dataset in features with their start and endlines [ageStart,ageEnd, genderStart, genderEnd, skillStart,skillEnd, weaknessSrart,weaknessEnd]
        self.clusters = [None] *(len(self.basicParameters)*2)

        self.parsePars()

        
    #parces Parameters.txt searching for parameters and their positions in Parameters.txt
    def parsePars(self):
        
        #returns parameters and clusters to their default values
        self.parameters = self.basicParameters.copy()
        self.clusters = [None] *(len(self.basicParameters)*2)

        with open(self.parametersPath,"r") as data:

         #index of the last element of the started cluster 
         indexOfClustersEnd = 0

         #defines whether an end of the list of feature values is being searched for
         inFeature = False

         for i, datapoint in enumerate(data):
            line = datapoint.strip()
                
            #Checks whether a feature is defined
            if(line != "" and inFeature == False):
                #Checks whether the feature is one of basic features(Age, Gender, Skill, Weakness)
                try:
                  t = self.parameters.index(line)
                  self.clusters[t*2] = i+1
                  indexOfClustersEnd = 2*t+1
                #If the feature is not basic adds it to the list
                except ValueError:
                  self.parameters.append(line)
                  self.clusters.append(i+1)
                  self.clusters.append(0)
                  indexOfClustersEnd = len(self.clusters)-1

                inFeature=True
            
            if(inFeature == True):
              self.clusters[indexOfClustersEnd] = i

            if(datapoint.strip() == ""):
              inFeature = False

    
    def generateRandomPlayer(self):
       
       #num of parameters
       numPars = len(self.parameters)

       #lines with stats
       randnumbers = [random.randrange(self.clusters[x*2],self.clusters[x*2+1]) for x in range(numPars)]
       
      #open parameters dataset       
       with open(self.parametersPath, "r") as data:

        #find a corresponding value for every parameter
        stats = {x : None for x in self.parameters}

        for i, element in enumerate(data):
          for n in range(numPars):
             if (i == randnumbers[n]):
              stats[self.parameters[n]] = element.strip()

        #create playercard
        pindex = 1
        if(len(self.players)>0):
          pindex = self.players[-1].index+1

        p = Playercard(pindex,**stats)
        self.players.append(p);    
    
    def deletePlayer(self, index):
        self.players = [p for p in self.players if p.index != index]

    def deleteAllPlayers(self):
      self.players = []


    def deleteParameter(self, parameter):

      if parameter in self.basicParameters:
        print(f"{parameter} is a basic parameter and cannot be deleted.")
      elif parameter not in self.parameters:
        print(f"Parameter {parameter} not found.")
      else:
        t = self.parameters.index(parameter)
        
        # remove from Parameters.txt
        with open(self.parametersPath, "r") as f:
          lines = f.readlines()
        
        del lines[self.clusters[t*2]-2 : self.clusters[t*2+1]]
        
        with open(self.parametersPath, "w") as f:
          f.writelines(lines)

          # remove from existing players
        for p in self.players:
          p.parameters.pop(parameter, None)

          # re-parse to rebuild clusters and parameters with correct indexes
        self.parsePars()
        print(f"{parameter} deleted.")

    
    def generateNewAIGame(self):
     results = []
    
     # generate base sections with fixed values
     for par in self.basicParameters:
        prompt = f"List 10 realistic values for the '{par}' attribute of a post-apocalyptic survivor. Output only the values, one per line, no numbers, no bullets, no extra text."
        response = rq.post("http://localhost:11434/api/generate", json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        })
        values = response.json()["response"].strip()
        results.append(f"{par}\n{values}")
    
     # generate 3 custom sections
     for i in range(3):
        prompt = f"Give me a single word attribute category for a post-apocalyptic bunker survivor character sheet. It must not be any of these: {self.parameters}. Examples of good categories: Condition, Background, Trait. Output only the word, nothing else."
        nameResponse = rq.post("http://localhost:11434/api/generate", json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        })
        name = nameResponse.json()["response"].strip()
        
        valuePrompt = f"List 10 realistic values for the '{name}' attribute of a post-apocalyptic survivor. Output only the values, one per line, no numbers, no bullets, no extra text."
        valueResponse = rq.post("http://localhost:11434/api/generate", json={
            "model": "llama3.2:3b",
            "prompt": valuePrompt,
            "stream": False
        })
        values = valueResponse.json()["response"].strip()
        results.append(f"{name}\n{values}")
        self.parameters.append(name)
    
     with open(self.parametersPath, "w") as f:
        f.write("\n\n".join(results))

     self.parsePars()
    
    def addAIParameter(self, name):
    
      if name in self.parameters:
        print(f"{name} already exists.")
        return False
      else:
       valuePrompt = f"List 10 realistic values for the '{name}' attribute of a post-apocalyptic survivor. Output only the values, one per line, no numbers, no bullets, no extra text."
       valueResponse = rq.post("http://localhost:11434/api/generate", json={
            "model": "llama3.2:3b",
            "prompt": valuePrompt,
            "stream": False
        })
       values = valueResponse.json()["response"].strip()

       with open(self.parametersPath,"a") as f:
        f.write(f"\n\n{name}\n{values}")

       self.parsePars()
       return True

      
      

    




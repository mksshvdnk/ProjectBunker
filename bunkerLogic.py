from pathlib import Path
import random



#A card of a player
class Playercard:
    def __init__(self,index, **kwargs):
        self.parameters = kwargs
        
#Gives player's parameters in a console
    def writePars(self):
        if self.parameters:
         print("\n".join(f"{key} : {value}" for key, value in self.parameters.items()))


#Generates player card based on given data  
class PlayerCardGenerator:
    def __init__(self):
        
        self.parametersPath = next(Path.cwd().rglob("Parameters.txt"),None)

        #list of all Players
        self.players : list[Playercard] = []

        #List of parameters
        self.parameters = ["Age", "Gender","Skill", "Weakness"]
        with open(self.parametersPath,"r") as data:
         
        
         #Clusters dataset in features with their start and endlines [ageStart,ageEnd, genderStart, genderEnd, skillStart,skillEnd, weaknessSrart,weaknessEnd]
         self.clusters = [None] *8

         #index of the last element of the started cluster 
         indexOfClustersEnd = 0

         #defines whether an end of the list of feature values is being searched for
         inFeature = False

         for i, datapoint in enumerate(data):
            line = datapoint.strip()
                
            #Checks whether a feature is defined
            if(line != ""):
             if(line[0] != '-'):
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
              stats[self.parameters[n]] = next((element.strip()[k:] for k, c in enumerate(element.strip()) if c.isalnum()))

        #create playercard
        p = Playercard(len(self.players)+1,**stats)
        self.players.append(p);    
      

    




from pathlib import Path
import random



#A card of a player
class Playercard:

    def __init__(self, age,gender, skill, weakness):
        self.age = age
        self.gender = gender
        self.skill = skill
        self.weakness = weakness
        
#Gives player's parameters in a console
    def writePars(self):
        print(f"Age:{self.age} \nGender {self.gender} \nSkill {self.skill} \nWeakness {self.weakness}")


#Generates player card based on given data  
class PlayerCardGenerator:
    def __init__(self):
        
        self.parametersPath = next(Path.cwd().rglob("Parameters.txt"),None)

        with open(self.parametersPath,"r") as data:
         self.players : Playercard = []
        
         #Clusters dataset in features with their start and endlines [ageStart,ageEnd, genderStart, genderEnd, skillStart,skillEnd, weaknessSrart,weaknessEnd]
         self.clusters = [None] *8

         #index of the last element of the started cluster 
         indexOfClustersEnd = 0

         #defines whether an end of the list of feature values is being searched for
         inFeature = False

         for i, datapoint in enumerate(data):
            match(datapoint.strip()):
                case "Age":
                  self.clusters[0] = i+1
                  indexOfClustersEnd = 1
                  inFeature = True
                case "Gender": 
                  self.clusters[2] = i+1
                  indexOfClustersEnd = 3
                  inFeature = True
                case "Skill":
                  self.clusters[4] = i+1
                  indexOfClustersEnd = 5
                  inFeature = True
                case "Weakness":
                  self.clusters[6] = i+1
                  indexOfClustersEnd = 7
                  inFeature = True
                  
            
            
            if(inFeature == True):
             self.clusters[indexOfClustersEnd] = i

            if(datapoint.strip() == ""):
             inFeature = False

    
    def generateRandomPlayer(self):
       #lines with stats
       randnumbers = [random.randrange(self.clusters[x*2],self.clusters[x*2+1]) for x in range(4)]
       
      #open parameters dataset       
       with open(self.parametersPath, "r") as data:

        #find stats with given numbers
        stats = [None]*4
        for i, element in enumerate(data):
          for n in range(4):
             if (i == randnumbers[n]):
              stats[n] = element.strip();

        #create playercard
        p = Playercard(*stats[:])
        self.players.append(p);    
      

    




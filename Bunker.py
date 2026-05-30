from pathlib import Path
import random


#Generates player card based on given data  
class PlayerCardGenerator:
    def __init__(self):
        self.data = open(next(Path.cwd().rglob("Parameters.txt"),None),"r")
        self.players : Playercard = []
        
        #Clusters dataset in features with their start and endlines [ageStart,ageEnd, genderStart, genderEnd, skillStart,skillEnd, weaknessSrart,weaknessEnd]
        self.clusters = [None] *8

        #index of the last element of the started cluster 
        indexOfClustersEnd = 0

        #defines whether an end of the list of feature values is being searched for
        inFeature = False

        for i, datapoint in enumerate(self.data):

            
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
       
       # Go back to beginning of file
       self.data.seek(0)

       #find stats with given numbers
       stats = [None]*4
       n = 0
       for i, element in enumerate(self.data):
          if i in randnumbers:
             #requires cluster to be sorted
             stats[n] = element.strip()
             n +=1

       #create playercard
       print(randnumbers) 
       print(stats)
       p = Playercard(*stats[:])
       self.players.append(p);    
      

    


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



pg = PlayerCardGenerator()
pg.generateRandomPlayer()
pg.players[0].writePars()

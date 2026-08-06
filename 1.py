name = "Neville"                     
signals = "gGhrGsgH"                 

signals = signals.lower()            

gryffindor = signals.count("g")      
hufflepuff = signals.count("h")    
ravenclaw = signals.count("r")       
slytherin = signals.count("s")      

houses = {                           
    "Gryffindor": gryffindor,
    "Hufflepuff": hufflepuff,
    "Ravenclaw": ravenclaw,
    "Slytherin": slytherin
}

max_count = max(houses.values())     

winners = []                         

for house in sorted(houses):         
    if houses[house] == max_count:   
        winners.append(house)        

winner = winners[0]                  

print(f"{name}, you belong in {winner}! ({max_count} signals)")
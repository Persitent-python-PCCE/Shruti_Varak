# The Sorting Hat receives a student's name and a mumbled string of house signals — letters it picked up from the student's
# personality. Each house is keyed by its first letter: Gryffindor, Hufflepuff, Ravenclaw, Slytherin. Count how often each
# house letter appears (case-insensitive) and sort the student into the house with the highest count. On a tie, choose the
#  house that comes first alphabetically.
name = "Neville"
signals = "gGhrGsgH"

signals = signals.lower()

g = signals.count("g")   
h = signals.count("h")   
r = signals.count("r")   
s = signals.count("s")   


houses = {
    "Gryffindor":g,
    "Hufflepuff":h,
    "Ravenclaw":r,
    "Slytherin":s
}


highest = max(houses.values())   


for i in houses:
    if houses[i]==highest:
     print(f"{name},you belong  in {i}! ({highest}signals)")
     break 







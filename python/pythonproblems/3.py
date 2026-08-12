goblin = ["Queens", "Manhattan", "Brooklyn", "Bronx"]
octopus = ["Manhattan", "Brooklyn", "Harlem"]
vulture = ["Manhattan", "Bronx", "Harlem"]

goblin = set(goblin)
octopus = set(octopus)
vulture = set(vulture)

common_turf = goblin & octopus & vulture
print("turf constested by all the three villians are", common_turf)

goblin_only = goblin - octopus - vulture
octopus_only = octopus - goblin - vulture
vulture_only = vulture - goblin - octopus

exactly_one = goblin_only | octopus_only | vulture_only
print("neigbourhoods held by exactly one villain", exactly_one)

distinct_neigh = goblin | octopus | vulture
count = 0

for i in distinct_neigh:
    count = count + 1

print("total distinct neigbours is ", count)
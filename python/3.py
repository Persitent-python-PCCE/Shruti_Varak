goblin = ["Queens", "Manhattan","Brooklyn", "Bronx"]
octopus = ["Manhattan", "Brooklyn","Harlem"]
vulture = ["Manhattan", "Bronx","Harlem"]




goblin_set =set(goblin)
octopus_set =set(octopus)
vulture_set = set(vulture)

contested = goblin_set & octopus_set & vulture_set

exactly_one=(
    (goblin_set - octopus_set - vulture_set)|
    (octopus_set - goblin_set - vulture_set)|
    (vulture_set - goblin_set - octopus_set)
    )

distinct = goblin_set | octopus_set | vulture_set

print("contested by all three:",contested)
print("constrolled by exactly one:",exactly_one)
print("distinct neighborhoods:",len(distinct))
# # (a) Common in all three
# # (b) Present in exactly one villain's territory
# # (c) Total distinct neighborhoods

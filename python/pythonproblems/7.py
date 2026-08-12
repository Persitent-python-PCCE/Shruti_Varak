# Write award_points(house, points=10, reason="general excellence", ledger=None) that records an award
# and returns the running ledger (a dictionary of house → total). The standard award is 10 points.
# The ledger must persist and accumulate across calls, while avoiding the mutable-default-argument problem.

def award_points(house, points=10, reason="general excellence", ledger=None):
    if ledger is None:
        ledger = {}

    if house in ledger:
        ledger[house] = ledger[house] + points
    else:
        ledger[house] = points

    print(house, "+", points, "(", reason, ") > total", ledger[house])

    return ledger


led = award_points("Gryffindor")
led = award_points("Gryffindor", 50, "defeating a troll", led)
led = award_points("Slytherin", 30, ledger=led)

print("Final ledger:", led)
def create_hero(name, *powers, **stats):

    print("Hero:", name)

    print("Powers:", ", ".join(powers))

    print("Stats:")

    total = 0
    count = 0

    for key, value in stats.items():
        print(f"{key}: {value}")
        total += value
        count += 1

    rating = total / count

    print(f"Overall rating: {rating:.1f}")

    if rating >= 90:
        print("S-Tier")


create_hero(
    "Spider-Man",
    "wall-crawl",
    "spider-sense",
    strength=85,
    agility=95,
    intelligence=92
)
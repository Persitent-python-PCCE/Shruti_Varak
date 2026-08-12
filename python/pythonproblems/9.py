def create_hero(name, *powers, **stats):
    print("Hero:", name)

    print("Powers:", ", ".join(powers))

    print("Stats:")
    for stat in stats:
        print(stat, ":", stats[stat])

    rating = sum(stats.values()) / len(stats)
    rating = round(rating, 1)

    print("Overall rating:", rating)

    if rating >= 90:
        print("> S-Tier *")


create_hero("Spider-Man", "wall-crawl",
            "spider-sense",
            strength=85, agility=95,
            intelligence=92)

create_hero("Spider-Man", "wall-crawl",
            "spider-sense",
            strength=85, agility=95,
            intelligence=92)
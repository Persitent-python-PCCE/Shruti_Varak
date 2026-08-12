teams = [
    ("Brazil", 3, 0, 0),
    ("Japan", 1, 2, 0),
    ("Spain", 2, 0, 1),
    ("Ghana", 0, 1, 2)
]   # team,wins,draws,losses
           # 3   1     0
qualified=[]

for team in teams:
      points = team[1] * 3 + team[2]
      losses = team[3]

      if points >= 6 and losses <=1:
       qualified.append(team)

print("advancing to knwolouts")

for team in qualified:
    points = team[1] * 3 + team[2]
    print(team[0], "-",points,"pts")
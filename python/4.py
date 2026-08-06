targets = [
    ("Falcon", 34.05, -118.24),
    ("Ghost", 99.9, 12.0),
    ("Condor", 40.71, -74.00)
]
valid_targets=[]

for target in targets:
    name,lat,lon =target

    if lat < -90 or lat >90 or lon < -180 or lon > 180:
        print(f"INVALID: {name} ({lat},{lon})")
    else:
        valid_targets.append(target)

 

print("\nBriefing (N >S):")
for target in valid_targets:
    name,lat,lon = target
    print(f"{name.upper()} > lat: {lat}, Lon: {lon}")

#     
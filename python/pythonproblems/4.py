targets = [
    ("Falcon", 34.05, -118.24),
    ("Ghost", 99.9, 12.0),
    ("Condor", 40.71, -74.00)
]   #name,lat,lon

valid_targets=[]
for target in targets:
    name = target[0]
    lat = target[1]
    lon = target[2]
    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
    #if lat < -90 or lat >90 or lon < -180 or lon >180:
        print("INVALID:",name,(lat,lon))
    else :
        valid_targets.append(target)


valid_targets.sort(key=lambda target:target[2],reverse =True)
    

for target in valid_targets:
    print(target[0].upper(),"->Lat: ",target[1],"Lon:",target[2])


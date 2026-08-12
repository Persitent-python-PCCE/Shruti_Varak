# Q2 — The Rush-Hour Report
# The Rush-Hour Report
# Kumar logs cups sold every hour from 8 AM onward. Build a small report from the list: the total cups, 
# the average per hour (rounded to 1 decimal), and every hour that beat the average — printed as the real
# clock hour (index 0 = 8 AM, index 1 = 9 AM, …). Those “rush hours” are the ones he'll staff extra help for.
cups = [12,5,8,20,3,15,22]


total = sum(cups)

average = round(total / len(cups),1)  

print("total:",total,"cups |average :",average,"/hr")


for i in range(len(cups)):  
   
        hour = 8 + i  
       

        if hour <12:
                time = f"{hour}AM"
        elif hour == 12:
                time = f"12PM"
        else:
                time = f"{hour - 12}PM"
                # 13 - 12 =1
                #14 -12 = 2
        print(time,end=",")





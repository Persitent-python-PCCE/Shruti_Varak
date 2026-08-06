cups = [12, 5, 8, 20, 3, 15, 22]          

total = sum(cups)                         
average = total / len(cups)               

print(f"Total: {total} cups | Average: {average:.1f}/hr")

print("Rush hours (above average):")

for i in range(len(cups)):                
    if cups[i] > average:                 
        hour = 8 + i                      

        if hour < 12:                     
            print(f"{hour} AM")
        elif hour == 12:                  
            print("12 PM")
        else:                             
            print(f"{hour - 12} PM")







orders = [
    ("Masala Chai",3,20),
    ("Samosa",2,15),
    ("Green Tea",1,30)
]
line_totals = list(map(lambda order: round(order[1] * order[2] * 1.05, 2), orders))
grand_total = sum(line_totals)
print("Line totals (incl.GST):", line_totals)
print(f"Grand total: Rs.{grand_total:.2f}")
  #sir solved problems after this try to understans that like  on probabiity
  # i mean not exactly but different kind on dictionaries and all
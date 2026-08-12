orders = [
    ("Masala Chai", 3, 20),
    ("Samosa", 2, 15),
    ("Green Tea", 1, 30)
]

# STEP 2 — "compute the line total
line_total=list(
 (map(lambda order: round((order[1]*order[2]) * 1.05,2),orders))
 )

grand_total=sum(line_total)

print("Line totals (incl.GST):",line_total)
print("grand total: Rs",grand_total)








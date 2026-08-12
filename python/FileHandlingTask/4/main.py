import csv

passed = 0
failed = 0
topper = ""
top_average = 0
results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        maths = int(row["maths"])
        physics = int(row["physics"])
        chemistry = int(row["chemistry"])

        total = maths + physics + chemistry
        average = total / 3

        # print(name, total, average)


        if average >= 90:
         grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        if average >= 40:
            passed += 1
        else:
            failed += 1

        if average > top_average:
            top_average = average
            topper = name

        
        results.append({
            "roll_no": row["roll_no"],
            "name": name,
            "maths": maths,
            "physics": physics,
            "chemistry": chemistry,
            "total": total,
            "average": round(average, 2),
            "grade": grade
        })

with open("students_result.csv", "w", newline="") as file:
    fieldnames = [
        "roll_no",
        "name",
        "maths",
        "physics",
        "chemistry",
        "total",
        "average",
        "grade"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)


print("Processed", len(results), "students -> students_result.csv")
print("Class Topper :", topper, "(avg", round(top_average, 2), ")")
print("Passed :", passed, "| Failed :", failed)
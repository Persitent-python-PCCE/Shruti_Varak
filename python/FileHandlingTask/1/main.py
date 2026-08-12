from log_utils import read_logs
from collections import Counter

logs = read_logs("app.log")

counter = Counter()

for level,message in logs:
    counter[level] += 1

errors=[]
for level,message in logs:
    if level=="Error":
        errors.append(message)

print("===log summary===")

print("INFO:",counter["INFO"])
print("WARNING",counter["WARNING"])
print("ERROR:",counter["ERROR"])
print("DEBUG :",counter["DEBUG"])

print()

print("Errors found:")

for error in errors:

    print(error)

#

with open("log_summary.txt","w") as file:

    file.write("=== Log Summary ===\n")

    file.write(f"INFO : {counter['INFO']}\n")
    file.write(f"WARNING : {counter['WARNING']}\n")
    file.write(f"ERROR : {counter['ERROR']}\n")
    file.write(f"ERROR : {counter['DEBUG']}\n\n")

    file.write("Errors found:\n")

    for error in errors:

        file.write(error+"\n")
# Python writing files (.txt, .json, .csv)

import json
import csv

employees = [["Name", "Age", "Job"], 
             ["Spongebob", 30, "Cook"], 
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
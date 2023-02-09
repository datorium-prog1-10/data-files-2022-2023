import csv

value_list = []

with open("atlase1.csv", encoding="utf8", mode="r") as file:
    for line in csv.DictReader(file, delimiter=";"):
        value_list.append(int(line[' E-pakalpojumu uzsākšanas reižu skaits']))

print(sum(value_list))
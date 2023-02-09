import csv

# csv fileused id Geeks.csv
filename = "list.csv"
 
# opening the file using "with"
# statement

main_list = []

with open(filename,'r') as data_file:
   for line in csv.DictReader(data_file):
      main_list.append(line)

print(main_list)
      
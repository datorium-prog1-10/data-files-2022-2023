import csv

with open("list.csv", "r") as file:
    csvFile = csv.DictReader(file)

    main_list = []

    for rinda in csvFile:
        main_list.append(rinda)

    print(main_list)
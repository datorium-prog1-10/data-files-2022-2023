#UZDEVUMS1
#Uzģenerē .CSV failu (datni)
#Operations with files


#1. Atvert failu rakstīšanai
file = open("list.csv", "w")
file.write("name, surname, email\n")

#2. Izveidot ciklu, un ierakstīt failā vēlamus datus
for i in range(1, 11):
    file.write(f"Name{i}, Surname{i}, Email{i}\n")

#3. Aizvert failu
file.close()
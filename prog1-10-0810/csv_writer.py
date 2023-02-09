#UZDEVUMS1
#Uzģenerē .CSV failu (datni)
#Operations with files

#1. Vajadzētu atvert failu rakstišanai
file = open("list.csv", "w")
file.write("name, surname, email\n")

#2. Ģenerēsim skatļus no 1 līdz 10
#to var izdarīt ar cikla plaīdzību
for i in range(1, 11):
    file.write(f"Name{i}, Surname{i}, Email{i}\n")

#3. Aizvert failu
file.close()
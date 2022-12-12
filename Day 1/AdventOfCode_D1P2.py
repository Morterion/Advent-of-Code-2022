file1 = open('input_d1.txt', 'r');
Lines = file1.readlines()
thislist = []
Calories = 0
indeksi = 0

for line in Lines:
    if line.strip(): #jos rivissä on jotain
        Calories += int(line)
        thislist.insert(indeksi, Calories)
    else: #jos rivi on tyhjä
        indeksi += 1
        Calories = 0

file1.close
thislist.sort()
print("Suurin paska:", thislist[-3]+thislist[-2]+thislist[-1])

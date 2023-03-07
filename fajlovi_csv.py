import csv

with open("studenti.csv", mode="r", encoding="utf-8", newline="") as myCsvFile:
    # reader vraca listu sa listama
    data = csv.reader(myCsvFile)
    print(data)
    for row in data:
        print(row[1])
    #print(*list(myCsvFile))

lista_studenata = []
with open("studenti.csv", mode="r", encoding="utf-8", newline="") as myCsvFile:
    # reader vraca listu sa listama
    data = csv.DictReader(myCsvFile)
    print(data)
    for row in data:
        lista_studenata.append(
            f'{row["ime"]} {row["prezime"]} | {row["indeks"]} | {row["smer"]}')
        print(row["indeks"])
    print(*lista_studenata)

lista_za_dodavanje = []
student_za_unos = {}
unos = input("Unesite podatke za studenta. Za prekid unosa unesite N.")
while unos != 'N':
    student = {
        "ime": "",
        "prezime": "",
        "indeks": "",
        "smer": ""
    }
    student["ime"] = input("ime: ")
    student["prezime"] = input("prezime: ")
    student["indeks"] = input("indeks: ")
    student["smer"] = input("smer: ")
    
    student_za_unos = student
    lista_za_dodavanje.append(student)
    unos = input("Novi student? Y/N: ")

with open("studenti.csv", mode="a", encoding="utf-8", newline="") as myCsvFile:
    fieldnames = ["ime", "prezime", "indeks", "smer"]
    writer = csv.DictWriter(myCsvFile, fieldnames=fieldnames)
    writer.writerows(lista_za_dodavanje)
    #writer.writerow(student_za_unos)
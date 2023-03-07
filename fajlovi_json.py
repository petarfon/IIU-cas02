import csv
import json

lista_studenata = {
    "studenti": []
}
with open("studenti.csv", mode="r", encoding="utf-8", newline="") as myCsvFile:
    # reader vraca listu sa listama
    data = csv.DictReader(myCsvFile)
    print(data)
    for row in data:
        lista_studenata["studenti"].append(row)

for dict in lista_studenata["studenti"]:
    print(dict, sep="\n")

with open("studenti.json", mode="w", encoding="utf-8", newline="") as myJsonFile:
    json.dump(lista_studenata, myJsonFile, ensure_ascii=False, indent=2)


with open("studenti.json", encoding="utf-8", mode="r") as myFile:
    data = json.load(myFile)
    print(*data["studenti"], sep="\n")

novi_student = {
    "ime": "Ivan",
    "prezime": "Ivanic",
    "indeks": "2017/1126",
    "smer": "MEN"
}

json_student = json.dumps(novi_student, ensure_ascii=False)
with open("test_student.json", mode="w", encoding="utf-8", newline="") as myJsonFile:
    myJsonFile.write(json_student)
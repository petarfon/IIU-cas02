import sqlite3
import csv


def kreiranje(conn):
    cur = conn.cursor()  # uvek se kreira kursor nad konekcijom kao i kod php-a
    query = """
        CREATE TABLE studenti(
            ime VARCHAR(255) NOT NULL,
            prezime VARCHAR(255) NOT NULL,
            indeks VARCHAR(10) NOT NULL,
            smer VARCHAR(4) NOT NULL
        );
    """
    cur.execute(query)
    conn.commit()
    cur.close()


def create(conn, student: tuple):
    cur = conn.cursor()  # uvek se kreira kursor nad konekcijom kao i kod php-a
    query = "INSERT INTO studenti VALUES(?,?,?,?)"

    # TUPLE
# c.execute("INSERT INTO employees VALUES (?,?,?)",(emp_1.first, emp_1.last, emp_1.pay))
    # DICTIONARY
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})
    cur.execute(query, student)
    conn.commit()
    cur.close()


def read(conn):
    cur = conn.cursor()  # uvek se kreira kursor nad konekcijom kao i kod php-a
    query = "SELECT * FROM studenti"
    cur.execute(query)
    lista = cur.fetchall()
    cur.close()
    return lista

# vratice sledeci red (i to samo 1 red, vraca None ako nema dalje)
# c.fetchone()

# prima parametar u vidu broja (vraca broj redova kao listu, a kad ne bude vise bilo redova vratice praznu listu)
# c.fetchmany(5)

# Vratice sve preostale redove i stavice ih u listu, a kad ne bude vise bilo redova vratice praznu listu
# c.fetchall()


def delete(conn, indeks):
    cur = conn.cursor()  # uvek se kreira kursor nad konekcijom kao i kod php-a
    query = f"DELETE FROM studenti WHERE indeks='{indeks}'"
    cur.execute(query)
    conn.commit()
    cur.close()


def main():
    # ova funkcija ce nam sluziti za testiranje
    conn = sqlite3.connect("studenti.db")
    # kreiranje(conn)  # zakomentarisemo nakon uspesnog kreiranja
    lista_studenata = []
    with open("studenti.csv", mode="r", encoding="utf-8", newline="") as std_fajl:
        # postavljamo newline="" kako nam se ne bi stvarali nepotrebni novi redovi
        # ovo nije mnogo bitno kod citanja koliko kod pisanja u csv fajl, gde je svaki red novi podatak
        reader = csv.DictReader(std_fajl)
        for row in reader:
            lista_studenata.append(row)
    # trebaju mi tuplovi da bih ubacio to u bazu kroz VALUES
    lista_tuplova = [tuple(st.values()) for st in lista_studenata]
    # print(lista_tuplova)
    create(conn, lista_tuplova[3])

    delete(conn, '2018/0801')
    print(read(conn))
    conn.close()


if __name__ == "__main__":
    # u slucaju da ovaj fajl pokrecemo kao glavni fajl
    #  python baza_studenti.py
    # u tom slucaju izvrsava se ovaj if, jer je njegovo ime __main__
    # da smo ga importovali negde, if se ne bi izvrsio, jer bi njegovo ime bilo ime fajla
    main()

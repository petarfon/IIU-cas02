import pickle

phonebook = {
    'Aleksa': '555-1234',
    'Marko': '555-5678',
    'Ana': '555-2468',
    'Pera': '555-1357',
}

out_file = open('phonebook.dat', 'wb')
pickle.dump(phonebook, out_file)
out_file.close()

in_file = open('phonebook.dat', 'rb')
phonebook1 = pickle.load(in_file)
in_file.close()
print(phonebook1)

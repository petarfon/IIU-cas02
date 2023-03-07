myFile = open('myfile.txt', 'w')

# print uvek ima novu liniju
# print("Name: ", myFile.name, end=" ")
print("Name: ", myFile.name)
print("Is closed: ", myFile.closed)
print("Opening mode: ", myFile.mode)

myFile.write('I love Python')
myFile.write(' and JavaScript\n')
myFile.close()

myFile = open('myFile.txt', 'a', encoding="utf-8")
myFile.write('I also like Đango!')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+', encoding="utf-8")
text = myFile.readline()
print(text)
myFile.seek(0)
text = myFile.read(20)
print(text)
#print(*list(myFile))

for line in myFile:print(line)

myFile.close()
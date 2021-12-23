from sys import argv

script, file_name = argv

print(f"{file_name} delete file.")
print("Cancel : CTRL-C (^C)")
print("Operate : Return Key(Enter)")

input("?")

print("Open a file...")
destination = open(file_name, 'w', encoding='utf-8')

print("Delete File. Good bye!")
destination.truncate()

print("Input new 3 lines")

line1 = input("line1 : ")
line2 = input("line2 : ")
line3 = input("line3 : ")

print("Write 3 line in File...")

destination.write(line1)
destination.write("\n")
destination.write(line2)
destination.write("\n")
destination.write(line3)
destination.write("\n")

print("Close a File...")
destination.close()

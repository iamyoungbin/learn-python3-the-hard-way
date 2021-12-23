from sys import argv

script, file_name = argv

text = open(file_name, encoding='utf=8')

print(f"file {file_name} :")
print(text.read())

print("Input file name once again.")
file_once = input("> ")

text_once = open(file_once, encoding='utf-8')

print(text_once.read())

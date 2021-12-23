from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hello {user_name}, i'm {script} Script.")
print("A few question.")
print(f"{user_name}. Like me?")
like = input(prompt)

print(f"{user_name}, Where do you live?")
live = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Ok, {like}
{live}
{computer}
""")

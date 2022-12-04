# MadLib Project

# To get an imput from cmd
# input is the key. It prints the string
# and get the imput from user to that variable

def get_name():
    return input("Enter a name: ")

def get_gerund():
    return input("Enter an ing verb: ")

def get_adjective():
    return input("Enter an adjective: ")

name = get_name()
gerund = get_gerund()
adjective = get_adjective()

madlib = "Hey, welcome to my " + name + " project. I think I can learn something " + adjective + " if I continue " + gerund
print(madlib)

madlibf = f"Hey, welcome to my {name} project. I think I can learn something {adjective} if I continue {gerund}"
print(madlibf)

def test_get_name():
    assert get_name() == ""

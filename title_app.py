def name_cap(name, surname):
    if name == "" and surname == "":
        return "Your input is not valid!"
    name1 = name.title()
    surname1 = surname.title()
    return f"{name1} {surname1}"
print(name_cap(input("Name:\n"),input("Surname:\n")))
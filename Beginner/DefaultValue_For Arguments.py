# We can include deffault value in the function argument

def get_gender(sex = "Unknowne"):
    if sex == "m":
        sex = "Male"
    elif sex == "f":
        sex = "Female"
    else:
        sex = "Unknowne"
    print(sex)

get_gender("m")
get_gender("f")
get_gender()
get_gender("Pate")
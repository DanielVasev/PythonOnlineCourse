"""
How we can extract min or max values from dictionary

"""
# we have out dictionary
grades = {

    "google": 434,
    "Aapl": 325,
    "FB":54,
    "AMZN": 623,
    "f": 32,
    "MSFT": 549

}

# printing min value by using MIN & ZIP
print(min(zip(grades.values(), grades)))
"""

When we want to execute a simple function with single atribute
"""

print("Base salary!")
salary = [16, 15, 22]
print(salary)


def new_salary(monay):
    return monay * 2

# We need to create new list where to store new salary after the increase

salary_after = list(map(new_salary, salary))

print("Salary after the increase")
print(salary_after)

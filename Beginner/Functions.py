def amaliaName():
    print("My name is Amalia and im awesome!")

def caculateGbpToBgn(GBP):
    amount = GBP * 2.20
    return amount

for n in range(100,1100,100):
    print("For ", n , " GBP you can take = ", caculateGbpToBgn(n), " BGN")

print(caculateGbpToBgn(970))

# girls age you can date Calculator
def calculator(myAge):
    results = myAge / 2 + 7
    return results

print(calculator(40))
magikNum = 13

# Exsample for break
for f in range(20):
    if f == magikNum:
        print("This is the magic Number ", f)
        # exsecution of the code will stop after F match magicNumber
        break
    else:
        print(f)

# Exsample for Continue/ meens will skip surton cases and continue with the code
num = [2,7,13,22]

for f in range(20):
    if f in num:
        print("skip")
        continue
    else:
        print(f)



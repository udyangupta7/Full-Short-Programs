import matplotlib.pyplot as plt
number = int(input("Enter the initial value to print the collatz sequence -"))
x, y, count = [0], [], 0
y.append(number)
def collatz(number):
    if number%2 == 0:
        return number//2
    elif number%2 == 1:
        return number*3+1
    else:
        print("Error Occurred")
        return None
while y[-1] != 1.0:
    count += 1
    x.append(count)
    y.append(collatz(y[-1]))
    print(y[-1], end="   ")
for i in list(zip(x, y)):
    plt.text(i[0], i[1], f"({i[0]} , {i[1]})")
plt.xlabel("Iterations")
plt.ylabel("Number (n)")
plt.title(f"Collatz Conjecture for n = {n}")
plt.plot(x, y, "bo-")
plt.show()
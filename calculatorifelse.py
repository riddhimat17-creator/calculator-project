print("simple calculator")
print("choose operation:")
print("1.addition(+)")
print("2. subtraction(-)")
print("3. multiplication(*)")
print("4. division(%)")
choice = input("enter choice(1/2/3/4)")
num1 = float(input("enter first number :"))
num2 = float(input("enter number 2:"))
if choice == "1" :
    result = num1+num2
    print("result", result)
elif choice == "2":
    result = num1-num2
    print("result",result)
elif choice == "3" :
    result = num1*num2
    print("result",result)
elif choice == "4" :
    if num2 == 0:
        print("error ! division by zero is not allowed")
    else:
        result = num1%num2
        print("result",result)
else:
    print("invalid input")
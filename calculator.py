def get_number(num):
    while True:
        operand = input("Number " + str(num) + ": ")
        try:
            return float(operand)
        except:
            print("Invalid input. Kindly try again.")

num_1 = get_number(1)
num_2 = get_number(2)
operator = input("Which operation do you want to perform? (+, -, *, /, %, **) ")

answer = 0

if operator == '+':
        answer = num_1 + num_2
        print(answer)
elif operator == '-':
        answer = num_1 - num_2
        print(answer)
elif operator == '*':
        answer = num_1 * num_2
        print(answer)
elif operator == '/':
        if(num_2 != 0):
            answer = num_1 / num_2
            print(answer)
        else:
            print("Number 02 can't be zero.")
elif operator == '%':
        if(num_2 != 0):
            answer = num_1 % num_2
            print(answer)
        else:
            print("Number 02 can't be zero.")
elif operator == '**':
        answer = num_1 ** num_2
        print(answer)
else:
        print("Invalid operation choosen.")
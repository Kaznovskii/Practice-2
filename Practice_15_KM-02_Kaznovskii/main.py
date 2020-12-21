from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import ln, log, lg


def main():
    print()
    print("Please, choose which function do you want to test.\n"
          "Type fact or exp2 or exp3 or root2 or root3 or ln or log or lg.")
    selected = input()
    if selected == "fact":
        n = input("Type number n: ")
        try:
            n = int(n)
            if n < 0:
                return "You entered not a natural number"
            else:
                return fact(n)
        except ValueError:
            return "You entered not a number."

    elif selected == "exp2":
        n = input("Type number n: ")
        try:
            n = float(n)
            return exp2(n)
        except ValueError:
            return "You entered not a number."

    elif selected == "exp3":
        n = input("Type number n: ")
        try:
            n = float(n)
            return exp3(n)
        except ValueError:
            return "You entered not a number."

    elif selected == "root2":
        n = input("Type number n: ")
        try:
            n = float(n)
            if n < 0:
                return "You entered not a positive number"
            else:
                return root2(n)
        except ValueError:
            return "You entered not a number."

    elif selected == "root3":
        n = input("Type number n: ")
        try:
            n = float(n)
            return root3(n)
        except ValueError:
            return "You entered not a number."

    elif selected == "log":
        a = input("Type base a: ")
        b = input("Type number b: ")
        try:
            a = float(a)
            b = float(b)
            if (b > 0) and (a > 0) and (a != 1):
                return log(b, a)
            else:
                return "a and b must be positive and a != 1."
        except ValueError:
            return "1 or more of your inputs are not a number."

    elif selected == "lg":
        b = input("Type number b: ")
        try:
            b = float(b)
            if b > 0:
                return lg(b)
            else:
                return "b must be positive."
        except ValueError:
            return "You entered not a number."

    elif selected == "ln":
        b = input("Type number b: ")
        try:
            b = float(b)
            if b > 0:
                return ln(b)
            else:
                return "b must be positive."
        except ValueError:
            return "You entered not a number."

    else:
        print("This function is not planned for testing :(")


if __name__ == '__main__':
    print(main())
#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = {"+": add, "-": sub, '*': mul, "/": div}

    if argv[2] not in list(op.key()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    
    a = argv [1]
    b = argv[3]

    print("{} {} {} = {}".format(a, argv[2], b, op[argv[2]](a, b)))

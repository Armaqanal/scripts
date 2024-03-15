import argparse


def summation(numbers):
    return sum(numbers)


def subtraction(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result


def multiplication(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def division(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result


parser = argparse.ArgumentParser()
parser.add_argument("--operation", choices=["summation", "subtraction", "multiplication", "division"], required=True)
parser.add_argument("numbers", type=float, nargs="+")
args = parser.parse_args()

if args.operation == "summation":
    print("result ->", summation(args.numbers))
elif args.operation == "subtraction":
    print("result ->", subtraction(args.numbers))
elif args.operation == "multiplication":
    print("result ->", multiplication(args.numbers))
elif args.operation == 'division':
    print("result -> ", division(args.numbers))
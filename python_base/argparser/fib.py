import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def Main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("num", help="The Fibonacci number " +
                        "you wish to calculate.", type=int)
    parser.add_argument("-o", "--output", help="Output the result to a file",
                        type=argparse.FileType(mode="w"))

    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print("Fib:" + str(result))
    elif args.quiet:
        print(result)
    else:
        print("F" + str(result))

    if args.output:
        args.output.write(str(result) + '\n')


if __name__ == '__main__':
    Main()

import argparse

from batfu.batfu import Batfu

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Obfuscate bat files')
    parser.add_argument('-i', '--input', type=str, help="Destination of input bat file")
    parser.add_argument('-o', '--output', type=str, help="Destination of output bat file")
    parser.add_argument('--min', type=int, help="Min length of variables", default=50)
    parser.add_argument('--max', type=int, help="Max length of variables", default=70)
    args = parser.parse_args()

    if args.input is None or args.output is None:
        print("Please specify input and output file.")
        exit(1)

    Batfu(args.input, args.output, args.min, args.max).run()

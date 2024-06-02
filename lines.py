from sys import argv, exit

def main():
    if len(argv) < 2:
        exit('Too few command_line arguments')
    elif len(argv) > 2:
        exit('Too many command_line arguments')
    else:
        if not argv.endswith('.py'):
            exit('Not a python file')
        else:
            print(count(argv[1]))


def count(file):
    try:
        lines = 0
        with open(file, 'r') as f:
            for line in f:
                if not (line.strip().startswith('#') or line.strip() == ''):
                    lines += 1
        return lines
    except FileNotFoundError:
        exit('File does not exist')


if __name__ == '__main__':
    main()
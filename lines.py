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
            pass


if __name__ == '__main__':
    main()
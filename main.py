keywords = ["IF", "WHILE"]

def main():
    f = open("text.txt")
    # Get lines from File
    lines = f.read().split('\n')
    # remove comments
    lines = [line.split('#', 1)[0] for line in lines]
    # remove blanks
    is_not_blank = lambda x: False if x == "" else True if x[0] not in [' ', '\n', '\t'] else is_not_blank(x[1:]);
    lines = list(filter(is_not_blank, lines))

    i = 0
    for l in lines:
        print(i, l)
        i = i+1
    

if __name__ == "__main__":
    main()

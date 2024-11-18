from enum import Enum

keywords = ["IF", "WHILE"]

class state(Enum):
    INDENTATION = None
    TOKEN = None

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
        print(l)
        depth = 0 #count of identation
        current_state = state.INDENTATION
        tokens = []
        while l != "":
            match current_state:
                case state.INDENTATION:
                    if(l[0] == '\t'):
                        depth+=1
                    else:
                        current_state=state.TOKEN
                        tokens.append("")
                case state.TOKEN:
                    if l[0] in [' ', '\t', '\n']:
                        tokens.append("")
                    else:
                        tokens[-1] = tokens[-1].join(l[0])
            l = l[1:]

        print("line: ", i, " depth: ", depth, "\ntokens: ", tokens)
        i = i+1

if __name__ == "__main__":
    main()

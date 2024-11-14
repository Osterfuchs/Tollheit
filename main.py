from enum import Enum

keywords = ["IF", "WHILE"]

class state(Enum):
    INDENTATION
    TOKEN

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
        depth = 0 #count of identation
        tokens = [""]
        current_state = state.INDENTATION
        while l != "":
            match current_state:
                case state.INDENTATION:
                    if(l[0] == '\t'):
                        depth+=1
                    else:
                        current_state=state.TOKEN
                        tokens.append()
                    break
                case state.TOKEN:
                    if l[0] in [' ', '\t', '\n']:
                        tokens.append()
                    else:
                        tokens[-1]+=l[0]
                    break
            l = l[1:]

        print("line: ", i, " depth: ", depth, " tokens: ", tokens)
        i = i+1

if __name__ == "__main__":
    main()

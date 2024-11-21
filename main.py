from enum import Enum

keywords = ["IF", "WHILE"]

class state(Enum):
    INDENTATION = 0
    TOKEN = 1
    UNKNOWN = 2
    NUMBER_LITERAL = 3
    

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
            if l[0] in [' ', '\t', '\n']:
                if current_state == state.INDENTATION:
                    depth+=1
                else:
                    current_state=state.UNKNOWN
            elif (l[0] >= 'a' and l[0] <= 'z') or (l[0] >= 'A' and l[0] <= 'Z') or (l[0] == '_'):
                if current_state == state.TOKEN:
                    tokens[-1] += l[0]
                else:
                    tokens.append(l[0])
                    current_state = state.TOKEN
            elif l[0] >= '0' and l[0] <= '9':
                if current_state == state.NUMBER_LITERAL:
                    tokens[-1] += l[0]
                else:
                    tokens.append(l[0])
                    current_state = state.NUMBER_LITERAL
            elif l[0] in ['(', ')', '{', '}', '[', ']']:
                tokens.append(l[0])
                current_state = state.UNKNOWN

            l = l[1:]

        print("line: ", i, " depth: ", depth, "\ntokens: ", tokens)
        i = i+1

if __name__ == "__main__":
    main()

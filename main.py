def main():
    f = open("text.txt")
    lines = list(filter(None, (line.split('#', 1)[0] for line in f.read().split('\n'))))
    i = 0
    for l in lines:
        print(i, l)
        i = i+1

if __name__ == "__main__":
    main()

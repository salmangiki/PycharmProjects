
def main():
    path = '/home/PycharmProjects/FileHandling/Task.py'
    f = open(path, 'r')
    g = open('file_write', 'w')
    total = [0] * len(f.readlines())
    count = 0
    last = '-'
    f.seek(0)
    for line in f:
        for word in line:
            if last != '-' and word.isdigit() is True:
                total[count] = total[count] + int(word)
            last = word
        print('Total of line %d is: %d' % (count+1, total[count]))
        g.write('Total of line %d is: %d\n' % (count+1, total[count]))
        count += 1


if __name__ == "__main__":
    main()

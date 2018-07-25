with open('my.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))

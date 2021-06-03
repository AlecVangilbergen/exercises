with open('attending.txt') as f:
    attending = set(line.strip().lower() for line in f)

with open('all.txt') as g:
    with open('absentees.txt', 'w') as out:
        for line in g:
            line = line.strip().lower()
            if line not in attending:
                print(line, file=out)

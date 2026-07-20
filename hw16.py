raw_input = input().split(';')
names = raw_input[0].split(',')
num = int(raw_input[1])

while names:
    idx = (num - 1) % len(names)
    removed_person = names.pop(idx)
    print(removed_person)
    names = names[idx:] + names[:idx]
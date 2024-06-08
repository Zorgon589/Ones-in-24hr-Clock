count = 0
minutes = 0
hours = 0


def con(input):
    x = str(input)
    return x.count('1')


while True:
    if minutes < 60:
        minutes = minutes + 1
        if con(minutes) > 0:
            count = count + 1
    elif minutes == 60:
        hours = hours + 1
        if con(hours) > 0:
            count = count + 1
        minutes = 0

    if hours is 24:
        print(count)
        break
    else:
        continue

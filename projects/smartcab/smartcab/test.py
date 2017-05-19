import random

if __name__ == '__main__':
    m = {}
    total = 384
    for i in range(total):
        m[i] = True
    count = 0
    while m:
        r = random.randrange(0, total)
        m.pop(r, None)
        count += 1
    print "For i of '{}' it took '{}' iterations".format(total, count)
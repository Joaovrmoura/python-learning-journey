def l(*args):
    for n in args:
        n += n
    return n

n = l(5, 9)

print(n)
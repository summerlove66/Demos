
def product(c):
    c.send(None)
    for i in range(10):

        c.send(i)


def consumer():

    while True:
        a = yield

        print(a)


product(consumer())

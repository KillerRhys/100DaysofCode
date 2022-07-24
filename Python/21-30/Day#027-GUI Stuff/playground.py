def add(*args):
    answer = sum(args)
    print(answer)

add(7, 5)

def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)
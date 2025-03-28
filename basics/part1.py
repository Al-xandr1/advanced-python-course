import math


def easy():
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(math.sqrt(a ** 10 + b ** 10))


def body_mass_index() -> None:
    mass = float(input())
    rost = float(input())

    i = mass / (rost * rost)

    if (i >= 18.5 and i <= 25):
        print("Оптимальная масса")
    elif (i < 18.5):
        print("Недостаточная масса")
    elif (i >= 25):
        print("Избыточная масса")


if __name__ == '__main__':
    body_mass_index()

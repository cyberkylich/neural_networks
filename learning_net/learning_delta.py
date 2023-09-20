x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
d = [1, -1, -1, -1]
# x1 = [-1, 1, -1, 1]
# x2 = [-1, -1, 1, 1]
# d = [-1, -1, -1, 1]
y = []
e = []

def learning():
    n = 1
    w1 = 0
    w2 = 0
    t = 0
    for j in range(4):
        net(w1, w2, x1[j], x2[j], t)
        e.append(d[j] - y[j])
        w1 = w1 + n * (d[j] - y[j]) * x1[j]
        w2 = w2 + n * (d[j] - y[j]) * x2[j]
        t = t + n * (d[j] - y[j]) * -1
        print("y = ", y[j], ", x1 = ", x1[j], ", x2 = ", x2[j], ", d = ", d[j])
        print("w1 = ", w1)
        print("w2 = ", w2)
        print("t = ", t)
        print("Ошибка : ", e[j])
        print("=============")
    test1 = int(input("Введите x1 : "))
    test2 = int(input("Введите x2 : "))
    net(w1, w2, test1, test2, t)
    print(y[-1])
    return


def net(w1, w2, x1, x2, t):
    s = w1 * x1 + w2 * x2 - t
    if s > 0:
        y.append(1)
        return s
    else:
        y.append(-1)
        return s



def main():
    learning()

    return


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt


x1 = [-1, 1, -1, 1]
x2 = [-1, -1, 1, 1]
y = [-1, -1, -1, 1]


def learning():
    w1 = 0
    w2 = 0
    t = 0
    # k = 0
    # while activation(w1, w2, x1, x2, t, k) != 1:
    #     k += 1
    for k in range(4):
        w1 = w1 + x1[k] * y[k]
        w2 = w2 + x2[k] * y[k]
        t = t - y[k]
        plt.scatter(x1[k], x2[k])
        plt.text(x1[k], x2[k] + 0.5, k + 1)
        print("Функция активации: ", activation(w1, w2, x1, x2, t, k))
        print("k = ", k + 1, ", x1 = ", x1[k], ", x2 = ", x2[k], ", y = ", y[k])
        print("w1 :", w1)
        print("w2 :", w2)
        print("t :", t)
        print("=======================================")
    return w1, w2, t


def activation(w1, w2, x1, x2, t, k):
    s = w1 * x1[k] + w2 * x2[k] - t
    if s > 0:
        plt.axline([0, 1], [1, 0])
        return 1
    else:
        return -1


def main():
    learning()
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()
    return


if __name__ == "__main__":
    main()

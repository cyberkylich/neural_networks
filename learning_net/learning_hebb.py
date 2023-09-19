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
        return 1
    else:
        return -1


def main():
    learning()

    return


if __name__ == "__main__":
    main()

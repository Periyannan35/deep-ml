def find_treasure(start_x: float) -> float:
    x = float(start_x)
    lr = 0.01
    beta = 0.9
    v = 0.0

    for _ in range(100000):
        grad = 4.0 * (x ** 3) - 9.0 * (x ** 2)
        if abs(x) < 1e-4 and abs(grad) < 1e-6:
            x += 0.01
            v = 0.0
            continue
        v = beta * v + grad
        x = x - lr * v

    return float(x)
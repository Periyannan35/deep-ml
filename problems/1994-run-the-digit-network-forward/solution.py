import numpy as np


def digit_network_forward(image, weights, biases):
    a = np.asarray(image, dtype=np.float64).ravel()
    for w, b in zip(weights, biases):
        w_arr = np.asarray(w, dtype=np.float64)
        b_arr = np.asarray(b, dtype=np.float64)
        z = w_arr @ a + b_arr
        a = 1.0 / (1.0 + np.exp(-z))
    rounded = [round(float(x), 4) for x in a]
    digit = int(np.argmax(a))
    return (rounded, digit)
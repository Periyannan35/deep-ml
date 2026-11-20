import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    squared_errors = []

    for x, y in zip(features, labels):
        z = sum(w * xi for w, xi in zip(weights, x)) + bias
        p = 1.0 / (1.0 + math.exp(-z))
        squared_errors.append((p - y) ** 2)
        probabilities.append(round(p, 4))
    mse = round(sum(squared_errors) / len(labels), 4)

    return probabilities, mse
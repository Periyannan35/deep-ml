import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    arr1=np.array(X,dtype=float)
    arr2=np.array(y,dtype=float)
    theta= np.linalg.inv(arr1.T @ arr1) @ (arr1.T @ arr2)
    return theta
import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    c=0
    for i in range(len(y_true)):
        if(y_true[i]==y_pred[i]):
            c+=1
    return c/len(y_true)
    pass
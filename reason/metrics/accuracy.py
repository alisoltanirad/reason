def accuracy(y_true, y_pred):
    all = len(y_true)
    correct = 0
    for i in range(all):
        if y_true[i] == y_pred[i]:
            correct += 1
    return float('{:.2f}'.format(correct / all))

def precision(tn, fp, fn, tp):
    """
    How many retrieved items are relevant
    """
    return tp / (tp + fp)


def recall(tn, fp, fn, tp):
    """
    How many  relevant items are retrieved
    """
    return tp / (tp + fn)


def f1(tn, fp, fn, tp):
    _precision = precision(tn, fp, fn, tp)
    _recall = recall(tn, fp, fn, tp)
    return 2 * (_precision * _recall) / (_precision + _recall)


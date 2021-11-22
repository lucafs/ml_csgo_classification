import pandas as pd

def prepare(dataset, column, max_value=None):
    lower, higher = dataset[column].min(), dataset[column].max()
    return lower, higher if not max_value else max_value


def build_numerical(dataset, col, lower, higher, n_bins):
    dataset = dataset[dataset[col] <= higher]
    edges = range(int(lower), int(higher), int((higher - lower) / n_bins))
    lbs = [i for i in range(len(edges) - 1)]
    return pd.cut(dataset[col], bins=n_bins, labels=lbs, include_lowest=True)


def build(dataset, col, lower, higher, n_bins):
    dataset = dataset[dataset[col] <= higher]
    edges = range(int(lower), int(higher), int((higher - lower) / n_bins))
    lbs = ["(%d, %d)" % (edges[i], edges[i + 1]) for i in range(len(edges) - 1)]
    return pd.cut(dataset[col], bins=n_bins, labels=lbs, include_lowest=True)
import pandas as pd

def load_dataset():
    return pd.read_csv("csgo_round_snapshots.csv")
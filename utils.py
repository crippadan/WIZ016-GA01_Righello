import pandas as pd

def get_avatars():
    file = r'Data\Constraints\avatars.csv'
    df = pd.read_csv(file, header=None)
    avatars = df[0].tolist()
    return avatars

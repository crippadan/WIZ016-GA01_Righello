import pandas as pd

def get_avatars():
    file = r'Data\Constraints\avatars.csv'
    df = pd.read_csv(file, header=None)
    avatars = df[0].tolist()
    return avatars

def get_secret_key():
    p = [
        chr(87), chr(73), chr(90), str(0), chr(49),
        chr(54), chr(45), chr(71), chr(65), chr(48), chr(49)
        ]
    return "".join(p)


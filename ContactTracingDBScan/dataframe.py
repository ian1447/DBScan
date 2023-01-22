import pandas as pd

col_names = ['Host', 'Port']
df = pd.DataFrame(columns=col_names)
df.loc[len(df)] = ['a', 'b']

t = df[df['Host'] == 'a']['Port'].item()
print(t)
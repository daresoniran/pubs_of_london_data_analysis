##pie chart

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('number_of_pubs_by_la.csv')
print(df.head(7))

# plt.figure(figsize=(5,5))

local_authority = df['Local Authority'].head(7)
num_of_pubs = df['Number of Pubs'].head(7)
colours = ['#e84e1b', '#2f3e58', '#ffdd00', '#ebe3dd', '#a9d9d9', '#5b2b3e', '#e7326d']

plt.pie(num_of_pubs,labels=local_authority, colors=colours)
plt.axis('equal')
plt.title('Seven Boroughs with the highest number of pubs')

plt.show()
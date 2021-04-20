## horizontal bar chart with mean line
## attempted to annotate the mean line

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('number_of_pubs_by_la.csv')
# print(df)


#plot
plt.barh(y=df['Local Authority'], width=df['Number of Pubs'], color='#2f3e58')
# plt.hist(x=df['Local Authority'], y=df['Number of Pubs'])

#title and labels
plt.title('Number of Pubs in London')
plt.ylabel('London Boroughs')
plt.xlabel('Number of Pubs')
plt.axvline(df['Number of Pubs'].mean(), color='#e84e1b', linewidth=2, linestyle='--')



plt.show()

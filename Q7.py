import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()

# Top 10 states with most homicides? 
print("Top 10 states with most homicides? ")
state = collections.Counter(data[:,5])
print(state)

#Plot Generator
objects = [state.most_common(10)[x][0] for x in range(10)]
performance = [state.most_common(10)[x][1] for x in range(10)]

y_pos = np.arange(len(objects))

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('Homicidesin state')
plt.title('Top 10 states with most homicides')
plt.savefig('Question7.png', bbox_inches='tight')
# Saved version is scaled so everything can be seen properly compared to "show" version
#plt.show()
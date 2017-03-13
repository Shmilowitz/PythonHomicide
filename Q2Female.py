import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()

# Which weapon is most used by men?
print("Which weapon is most used by men?")
mask = (data[:,15] == 'Female')
wep = collections.Counter(data[mask][:,20])
print(wep)

#Plot Generator
objects = [wep.most_common(16)[x][0] for x in range(16)]
performance = [wep.most_common(16)[x][1] for x in range(16)]

y_pos = np.arange(len(objects))

plt.bar(y_pos, performance, align='center', alpha=0.5)
for a,b in zip(y_pos, performance):
	plt.text(a-0.25, b+30000, str(b), rotation=90)
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('Times that the weapon is used')
plt.title('Which weapon is most used by females?')
plt.savefig('Question2ChartFemale.png', bbox_inches='tight')
# Saved version is scaled so everything can be seen properly compared to "show" version
#plt.show()
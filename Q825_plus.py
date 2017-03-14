import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()

# Are younger perpetrators (age 15-25) more likely to get caught then older ones (25+)?
print("Top 10 states with most homicides? ")
mask25_plus = (data[:,16] > 25) 
caught25_plus = collections.Counter(data[mask25_plus][:,10])
print(caught25_plus)

# Plot Generator
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.3f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
labels = '+25 caught', '+25 not caught',
performance = [caught25_plus.most_common(2)[0][1], caught25_plus.most_common(2)[1][1]]
fig1, ax1 = plt.subplots()
ax1.pie(performance, labels=labels, autopct=make_autopct(performance),shadow=True, startangle=45)
ax1.axis('equal')
plt.title("+25 getting caught")
plt.savefig('Question825_plus.png') 
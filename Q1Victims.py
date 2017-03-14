import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()
# Which ethnicity is it most common for the victims and perpetrators to be?
print("Which ethnicity is it most common for the victims and perpetrators to be?")
ethni = collections.Counter(data[:,14])
print(ethni)

# Plot Generator

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
labels = 'Unknown', 'Non-Hispanic', 'Hispanic'
explode = (0.1, 0,0.0)
performance = [ethni.most_common(10)[0][1],ethni.most_common(10)[1][1], ethni.most_common(10)[2][1]]
fig1, ax1 = plt.subplots()
ax1.pie(performance,explode=explode, labels=labels, autopct=make_autopct(performance),shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Most commmon ethnicity groups for victims")
plt.savefig('Question1ChartVictim.png')
#plt.show()
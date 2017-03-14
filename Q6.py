import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()

#Male to female ratio of perpetrators?
maskMale = (data[:,15] == 'Male')
maskFemale = (data[:,15] == 'Female')
Maleperp = data[maskMale].size
Femaleperp = data[maskFemale].size
print('Male perpetrators: ', Maleperp)
print('Female perpetrators: ', Femaleperp)

#Plot Generator
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
labels = 'Male', 'Female'
performance = [Maleperp,Femaleperp]
fig1, ax1 = plt.subplots()
ax1.pie(performance, labels=labels, autopct=make_autopct(performance),shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Male to female ratio of perpetrators")
plt.savefig('Question6.png')
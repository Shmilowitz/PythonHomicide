import pandas as pd
import numpy as np
import sys

database = pd.read_csv("database.csv", low_memory=False)

#Average age of victims?
ages = database['Victim Age']
print("Average age of victim: ", "%.1f" % np.mean(ages))
sys.stdout = open('Q5.txt', 'w')
print("Average age of victim: ", "%.1f" % np.mean(ages))
sys.stdout.close()



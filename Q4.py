import pandas as pd
import numpy as np
import sys

database = pd.read_csv("database.csv", low_memory=False)
#Youngest and oldest victims
ages = database['Victim Age']
sys.stdout = open('Q4.txt', 'w')
print("Youngest Victim: ", np.amin(ages))
print("Oldest Victim: ", np.amax(ages))
sys.stdout.close()
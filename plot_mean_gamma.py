import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate

data = ['gamma_6Mev.txt', 'gamma_7Mev.txt', 'gamma_8Mev.txt', 'gamma_9Mev.txt', 'gamma_10Mev.txt']

# Open the input file for reading

with open(data[4], 'r') as file:
    myArray = []
    # Read the file line by line
    for line in file:
        # Split the line into columns using whitespace as the delimiter
        columns = line.split()

        # Check if there are at least three columns in the line
        if len(columns) >= 1:
            # Get the first three columns
            col1 = float(columns[0])
            
            myArray.append([col1])

# Close the file when done
file.close()
newArray = np.array(myArray)

plt.hist(newArray, bins = 20)
plt.xlabel('Gammas per event')
plt.title('Mean gamma multiplicity, gun_230Ac_10MeV')
plt.savefig('mean_gamma_10MeV.pdf')
    

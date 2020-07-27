# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns



# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_= plt.hist(versicolor_petal_length)

plt.xlabel('petal length (cm')
plt.ylabel('count')

# Show histogram
plt.show()


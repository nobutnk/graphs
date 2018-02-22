import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test/test1.csv', names=['num1', 'num2'])
plt.plot(range(0,10), df['num2'], marker="o")
plt.show()

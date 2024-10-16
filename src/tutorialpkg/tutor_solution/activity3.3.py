import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
print(df)
df.boxplot()
df.plot.box()  # This syntax is also valid
plt.show()

# df.groupby("ColNameToGroupBy").plot(x="SomeCol", y="AnotherCol")
# df.groupby("A").plot(x="A", y="B")
# plt.show()
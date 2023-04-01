import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(6, 4),
                  columns=pd.Index(['A', 'B', 'C', 'D'],
                  name='Genus'))
print(df)
df.plot.bar()
plt.show()

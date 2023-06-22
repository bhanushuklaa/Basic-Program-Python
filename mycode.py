import pandas as pd
import numpy as np
 
NaN = np.nan
 
company = [(1100, 10000, 40, 200),
           (1200, 5000, NaN, NaN),
           (500, 600, 60, 500),
           (3000, 3000, NaN, 700),
           (5000, 4000, 50, 700)
           ]
 
df = pd.DataFrame(company, columns=['INCOME1', 'INCOME2', 'INCOME3', 'INCOME4'])
 
print(df)
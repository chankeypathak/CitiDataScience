#!/usr/bin/env python3
import pandas as pd
import numpy as np

df = pd.DataFrame(["blue","green","red"], columns = ["A"])
print (df)

df ['A'] = df['A'].astype('category')
df['A_cat'] = df['A'].cat.codes
print (df)



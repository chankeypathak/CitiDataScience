#!/usr/bin/env python3
import pandas as pd
import numpy as np

df = pd.DataFrame(list(zip(["Model1", "Model2", "Model3"],["blue","green","red"])), columns = ["Model Name","Model Color"])
print (df)

print (pd.get_dummies(df,columns=['Model Color']))




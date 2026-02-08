import pandas as pd

    
def null( df):
    na =df.isnull().sum()
    ratio = na / df.shape[0]
    return pd.DataFrame({'Null' :na ,'Ratio' :ratio}).T
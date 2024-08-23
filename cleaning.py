import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')
# new_df = df.dropna()  #return data with no empty cells
# df.dropna(inplace = True) # if we want to change original data
# df.fillna(130, inplace = True)  # replaces null values with 130 / inplace true changes org dataframe
# df["abc"].fillna(130, inplace = True) # changes to specific column i.e. abc
# x = df["abc"].mean()
# x = df["abc"].median()
# x = df["abc"].mode()
# df["abc"].fillna(x, inplace = True) # replace empty cell with mean/median/mode value
# print(new_df.to_string())

# df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace = True)
# print(pd.to_datetime(df['Date']))
# print(df.to_string())

#handling wrong data:
# for x in df.index:
#   if df.loc[x, "Duration"] > 60:
#     df.loc[x, "Duration"] = 60

# or remove datas which have value more than 60
# for x in df.index:
#   if df.loc[x, "Duration"] > 60:
#     df.drop(x, inplace = True)

#duplicate values
# print(df.duplicated())
# df.drop_duplicates(inplace = True)


#correlations
# df.corr()   #shows reln bertn columns

#plots
# df.plot()
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
df['Duration'].plot(kind = 'hist')
plt.show()



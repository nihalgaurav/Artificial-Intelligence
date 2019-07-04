import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, 15, 7, 8, np.nan])
print(s)


dates = pd.date_range('20190101', periods=6, freq='D')  # D- daily , M- monthly, Y- yearly

print(dates)  # it contains 6 dates as array
print(dates[0])

print(np.random.randn(6,4))  # no meta data

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])  # dates are index heading
print(df)
print("Headings in Dataframe : \n", df.columns )
print(" Row heading in data frame : \n", df.index )
print(" values in dataframe : \n", df.values )

df2 = pd.DataFrame({'A' : 1.0,
                    'B' : pd.Timestamp("20190102"),
                    'C' : pd.Series(1, index=list(range(4)), dtype='float64'),
                    'D' : np.array([3]*4, dtype='int64'),
                    'E' : pd.Categorical(['test', 'IITK', 'train', 'test'], categories=['test', 'train']),
                    # here iitk generates nan
                    'F' : 'foo'})

print(df2)
# a = pd.Categorical(['test', 'train', 'train', 'test', 'sip'], categories=['test', 'train'])
# print(a)

print(df2.dtypes)
print(df.head())  # default top 5 values
print(df.tail())  # default last 5 value
print(df.sample(3))  # random 1 values
print(df.describe())  # will not include text
print(df.describe(include='all'))  # will include text too
print(df.T)  # print transpose

print("\n\n original Values : \n", df)
print("\n\n df.sort_index(axis=1, ascending=False) : \n\n", df.sort_index(axis=1, ascending=False))

print("sorted values : \n\n", df.sort_values(by='B', ascending=True))


print()
print(df.A)
print()
print(df['A'], '\n\n')


print('\n\n', df['2019-01-01':'2019-01-06':2])
print('\n\n', df[0::2])

print('\n\n', df['20190102':'20190104'])

print('\n\n', df.loc[dates[0]])

print('\n\n', df.loc[:, ['A', 'B']])

print('\n\n', df.loc['20190102':'20190104', ['A', 'B']])

print('\n\n', df.loc['20190102', ['C', 'D']])

print('\n\n', df.loc[dates[0],'A'])
print('\n\n', df.at[dates[0],'A'])  # faster than loc but has no difference

print('\n\n', df.iloc[3])
print('\n\n', df.iloc[3:5, 0:2])
print('\n\n', df.iloc[[1, 2, 4], [0, 2]])

print('\n\n', df.iloc[1:3,:])
print('\n\n', df.iloc[:, 1:3])

# print('\n\n', df.iloc[1, 1])
print('\n\n', df.iloc[1, 1])
print('\n\n', df.iat[1, 1])  # faster than iloc but has no difference

# boolean indexing

print('\n\n', df.A)

print('\n\n', df.A > 0)
print('\n\n', df[df.A > 0])  # this is similar to the line below not by the value but by the syntax
print('\n\n', df[[True, True, False, True, False, True]])  # index having true will get printed

print('\n\n', df[df.A > 0]['B'])
print('\n\n', df[df.A > 0]['B'].mean())

"""
dataframe catalog 보기
"""
import pandas as pd 

df = pd.read_csv('laptops.csv')

# 위에서 6개 record만 보기 
print('위에서 6개 record만 보기 -head\n {}'.format(df.head(6)))

# 밑에서 6개 record만 보기 
print('밑에서 6개 record만 보기 - tail\n {}'.format(df.tail(6)))

#dataframe size보기 
print('dataframe size 보기 - shape\n {}'.format(df.shape))

#dataframe columns보기 
print('dataframe columns 보기 - columns\n {}'.format(df.columns))

#dataframe inforamtion 보기 
print('dataframe information 보기 - info\n {}'.format(df.info()))

#dataframe 통계정보 보기 
print('dataframe 통계정보 보기 - describe\n {}'.format(df.describe()))

#dataframe 정렬하기 
print('dataframe 정렬하기 - sort_values(by=colname,[ascending=False])\n {}'.format(df.sort_values(by='price',ascending=False,inplace=True)))


### Series 
# unique한 값만 보기 

print('dataframe Series unique한 값만보기  df[col].unique()\n {}'.format(df['brand'].unique()))

# unique한 값 count 보기 
print('dataframe Series unique한 값 record count만보기  df[col].value_counts()\n {}'.format(df['brand'].value_counts()))

# Series describe 
print('dataframe Series describe 정보  df[col].describe()\n {}'.format(df['brand'].describe()))




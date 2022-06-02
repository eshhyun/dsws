import pandas as pd

df = pd.read_csv('liverpool.csv',index_col=0)
print(df)

"""
                position  born  number nationality
name
Roberto Firmino       FW  1991   no. 9      Brazil
Sadio Mane            FW  1992  no. 10     Senegal
Mohamed Salah         FW  1992  no. 11       Egypt
Joe Gomez             DF  1997  no. 12     England
Alisson Becker        GK  1992  no. 13      Brazil
"""

"""
 column name이 소문자로 시작되는 것을 대문자로 시작되는 것으로 column을 변경
"""

df.rename(columns={'position':'Position','born':'Born', 'number':'Number','nationality':'Nationality'} , inplace=True)
print(df)


"""
index name을 변경 
"""
df.index.name = 'Palyer Name'
print(df)


"""
Index field를 변경 
기존 index field를 신규 column에 추가한 뒤 기존 col 중 하나를 선택해서 index를 변경한다. 
"""

df['Palyer Name'] = df.index
df.set_index('Number',inplace=True)

print(df)


"""
각 파트가 최소 250점, 총 점수가 최소 600점이 되어야 서류 전형을 합격할 수 있습니다.

기존 DataFrame에 “합격 여부”라는 column을 추가하고, 합격한 지원자는 불린 값 True, 불합격한 지원자는 불린 값 False를 넣어주면 됩니다.
"""
df = pd.read_csv('toeic.csv')

pass_total = df['LC'] + df['RC'] >= 600
pass_both = (df['LC'] >=250)  & (df['RC'] >= 250)

df['합격여부']= pass_total & pass_both  


"""
 df set 변경 
"""

df = pd.read_csv('puzzle.csv')

# 코드를 작성하세요.

print(df)

df['A'] = df['A'] *2 

print(df)
print(df.loc[:,'B':'E'])

df[df.loc[:, 'B':'E'] < 80] = 0
df[df.loc[:, 'B':'E'] >= 80] = 1


df.loc[2,'F'] = 99


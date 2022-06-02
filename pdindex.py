"""
지난 시간에 DataFrame에서 원하는 부분을 선택하는 인덱싱을 배웠는데요. 이를 통해서 값을 찾는 연습을 해봅시다.
2016년도에 KBS방송국의 시청률을 찾아봅시다.
데이터를 한번 잘 살펴보고 어떻게 값을 찾아야 할지 고민해보세요!
"""

import pandas as pd

df = pd.read_csv('broadcast.csv', index_col=0)

print(df.loc[2016, 'KBS']) # 2016년 row에 KBS col 찾기 


"""
JTBC 전체 시청율 
"""
print(df.loc[:,'JTBC'])  # : row 전체 , col은 jtbc 인것 


"""
이번에는 DataFrame에서 여러 줄을 찾는 연습을 해보겠습니다. 
SBS와 JTBC의 시청률만 확인하려면 어떻게 하면 될까요?
"""

print(df.loc[:,['SBS','JTBC']])  # : row 전체 , col은 jtbc, SBS 인것 
print(df[['SBS','JTBC']])        #   row 전체 선택시 loc 없이 df 자체를 indexing 한다. 


"""
이번에는 DataFrame에서 연속된 여러 줄을 찾는 연습을 해보겠습니다.

방송사는 'KBS'에서 'SBS'까지, 연도는 2012년부터 2017년까지의 시청률만 확인하려면 
"""

print(df.loc['2012': '2017','KBS':'SBS'])

"""
'KBS'에서 시청률이 30이 넘은 데이터만 확인해보려면 어떻게 하면 될까요?
"""

print(df.loc[df['KBS'] > 30,'KBS'])


boolean_KBS = df['KBS'] > 30
df.loc[boolean_KBS, 'KBS']


"""
주어진 데이터에서 SBS가 TV CHOSUN보다 더 시청률이 낮았던 시기의 데이터를 확인
"""
condition = df['SBS'] < df['TV CHOSUN']
df.loc[condition,['SBS' ,'TV CHOSUN']]

"""
DataFrame 인덱싱을 하는 방법과 종류가 많아서 헷갈리기 쉽습니다.

인덱싱이 익숙해져야 다음 내용을 쉽게 배울 수 있으니, 꼭 숙지하고 넘어가세요!


이름으로 인덱싱하기	기본 형태	단축 형태

-하나의 row 이름	df.loc["row4"]	
-row 이름의 리스트	df.loc[["row4", "row5", "row3"]]	

-row 이름의 리스트 슬라이싱	df.loc["row2":"row5"]	df["row2":"row5"]
-하나의 column 이름	df.loc[:, "col1"]	df["col1"]
-column 이름의 리스트	df.loc[:, ["col4", "col6", "col3"]]	df[["col4", "col6", "col3"]]
-column 이름의 리스트 슬라이싱	df.loc[:, "col2":"col5"]	

위치로 인덱싱하기	기본 형태	단축 형태

-하나의 row 위치	df.iloc[8]	
-row 위치의 리스트	df.iloc[[4, 5, 3]]	
-row 위치의 리스트 슬라이싱	df.iloc[2:5]	df[2:5]
-하나의 column 위치	df.iloc[:, 3]	
-column 위치의 리스트	df.iloc[:, [3, 5, 6]]	
-column 위치의 리스트 슬라이싱	df.iloc[:, 3:7]

"""


"""
해야 할 일이 세 가지 있습니다.

ID 1의 무게를 200으로 변경하세요.
ID 21의 row를 삭제하세요.
ID 20의 row를 추가하세요. ID 20의 키는 70, 무게는 200입니다.

ID,Height (Inch),Weight (Pound)
0,73.847017017515,241.893563180437
1,70,

"""

body_df = pd.read_csv('body.csv',index_col=0)


body_df.loc[1,"Weight (Pound)"] = 200

body_df.drop(21,axis='index',inplace=True) # axis : index => row , column = col , inplace : true df 실제 update, false는 수행시에만 적용 

body_df.loc[20] = [20,70,200]

"""
아기의 성별과 어머니의 인종에 따른, 뉴욕에서 가장 인기 있는 아기 이름이 무엇인지 조사를 해 봤습니다.

조사 결과가 data 폴더의 popular_baby_names.csv라는 파일에 담겨 있는데요. 안에 있는 정보를 DataFrame으로 읽어 들이고, DataFrame을 출력해 주세요.


"""
import pandas as pd

df = pd.read_csv('./popular_baby_names.csv')

print(df)

"""
 read_csv(datafile, options)

 1) csv파일내 header가 없는 경우 
       
iphone1,iphonex2 version,1990-01-01

 read_csv(datafile,header=None)
 => column name이 0,1,2,3,4,5 형태로 추가된다.
"""

df_noheader=pd.read_csv('iphone_noheader.csv')
print(df_noheader)




"""
 2) Header에 col이 생략된경우 
  ,description,releasedate 
  iphone1,iphonex2 version,1990-01-01

 read_csv(datafile,index_col=0)
 => index에 순자 번호가 아닌 column zerork index indexid가 된다.

"""

   
df_nocol=pd.read_csv('iphone.csv',index_col=0)
print(df_nocol)


"""
메가밀리언 측에서 2002년부터 현재(2/15/19)까지의 당첨 번호가 담긴 mega_millions.csv 파일을 공개했는데요. 이 데이터를 DataFrame에 넣어 봅시다.

날짜(Draw Date)가 이 DataFrame의 인덱스가 되도록 해 주세요!
"""

df = pd.read_csv('./data/mega_millions.csv',index_col=0) 
# df = pd.read_csv('./data/mega_millions.csv',index_col='Draw Date') 도 동일함 

print(df)
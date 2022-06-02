import pandas as pd 

"""
아래와 같은 결과가 나오도록 DataFrame을 만들고 출력해 보세요.  
column은 name, birthday, occupation 총 3개입니다.

name	birthday	occupation
0	Taylor Swift	December 13, 1989	Singer-songwriter
1	Aaron Sorkin	June 9, 1961	Screenwriter
2	Harry Potter	July 31, 1980	Wizard
3	Ji-Sung Park	February 25, 1981	Footballer

"""

df = pd.DataFrame([['Taylor Swift' ,	'December 13, 1989',	'Singer-songwriter']
,['Aaron Sorkin',	'June 9, 1961'	,'Screenwriter']
,['Harry Potter',	'July 31, 1980'	,'Wizard']
,['Ji-Sung Park',	'February 25, 1981',	'Footballer']
],columns=['name','birthday','occupation'],index=['0','1','2','3'])

print(df)

"""
pandas DataFrame에는 다양한 종류의 데이터를 담을 수 있습니다. dtypes를 사용해서 각 column이 어떤 데이터 타입을 보관하는지 확인할 수 있는데요.


pandas의 dtype들
pandas에 담을 수 있는 dtype(데이터 타입) 몇 가지를 살펴봅시다.

dtype	설명
int64	정수
float64	소수
object	텍스트
bool	불린(참과 거짓)
datetime64	날짜와 시간
category	카테고리

"""
import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])

print(my_df.dtypes)

"""
name             object
english_score     int64
math_score        int64
dtype: object
위 경우 'name' column은 object라는 데이터 타입을 보관하고, 'english_score'와 'math_score' column은 int64라는 데이터 타입을 보관하는 거죠.

보시다시피 한 column 내에서는 모든 값이 동일한 데이터 타입입니다.

"""
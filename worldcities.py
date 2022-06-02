
import pandas as pd

df = pd.read_csv('world_cities.csv',index_col=0)
df.index.name='seq'

"""
주어진 데이터에는 총 몇 개의 도시와 몇 개의 나라가 있는지 알아맞혀 보세요.

답안은 도시/나라 형식으로 숫자만 입력해 주세요. (예시: 156/77)
"""

df['City / Urban area'].value_counts().shape
df['Country'].value_counts().shape

"""
사람 만나기를 좋아하는 익중이는 가장 사람이 붐비는 도시로 여행을 가기로 마음 먹었습니다. 주어진 데이터에서, 
인구 밀도(명/sqKm) 가 10000 이 넘는 도시는 총 몇 개인지 알아보세요.

참고로 인구 밀도는 인구 수 / 땅의 면적 (in sqKm) 로 구할 수 있습니다.
Population	Land area (in sqKm)

"""

df['Density'] = df['Population'] / df['Land area (in sqKm)']
high_density_df = df[df['Density']>10000]
high_density_df.info()


"""
이번에는 인구 밀도가 가장 높은 도시를 찾아봅시다.
"""

density_ranks = high_density_df.sort_values(by='Density',ascending=False)
print( density_ranks['City / Urban area'] )


"""
익중이는 누나에게 여행지를 추천 받으려고 합니다.
그런데 나라 이름이 기억나지 않고, 이 데이터에 4개의 도시가 나왔다는 것만 기억이 난다고 하네요.
이 나라는 무엇일까요?

답안은 데이터에 적힌 이름 그대로 적어 주세요. (예시: France)
"""

countries = df['Country'].value_counts()
print(countries[countries==4])

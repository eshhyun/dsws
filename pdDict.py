"""

두 카드사는 사람들이 요일별로 지출하는 평균 금액을 “요일”, “식비", “교통비”, “문화생활비”, “기타” 카테고리로 정리해서 우리에게 공유해 주기로 했는데요. 각각 samsong.csv 파일과 hyundee.csv 파일을 보냈습니다.

두 회사의 데이터를 활용해서, 사람들의 요일별 문화생활비를 분석해보려 합니다. 아래와 같은 형태로 출력이 되도록 DataFrame을 만들어보세요.

 day  samsong  hyundee
0  MON     4308     5339
1  TUE     7644     3524
2  WED     5674     5364
3  THU     8621     9942
4  FRI    23052    33511
5  SAT    15330    19397
6  SUN    19030    19925

"""

import pandas as pd

samsong_df = pd.read_csv('sam.csv')
hyundee_df = pd.read_csv('hyun.csv')

s_slice = samsong_df.loc[:,"문화생활비"]
h_slice = hyundee_df.loc[:,"문화생활비"]

combind_df = pd.DataFrame(
  {
    'day': samsong_df['요일'],
    'samsong': samsong_df['문화생활비'],
    'hyundee': hyundee_df['문화생활비']
  }
)

print(combind_df)
"""
2,000명의 코드잇 대학교 학생들이 수강신청을 했습니다.

수강신청에는 다음 3개의 조건이 있습니다.

“information technology” 과목은 심화과목이라 1학년은 수강할 수 없습니다.
“commerce” 과목은 기초과목이고 많은 학생들이 듣는 수업이라 4학년은 수강할 수 없습니다.
수강생이 5명이 되지 않으면 강의는 폐강되어 수강할 수 없습니다.
기존 DataFrame에 “status”라는 이름의 column을 추가하고, 학생이 수강 가능한 상태이면 “allowed”, 수강 불가능한 상태이면 “not allowed”를 넣어주세요.
"""
import pandas as pd 

df = pd.read_csv('enrolment_1.csv')

df['status']='allowed'
#id,year,course name
boolean1 = df['course name'] == 'information technology'  
boolean2 = df['year'] == 1 
df.loc[boolean1 & boolean2,'status'] = "not allowed"

# or 
#df.loc[ (df['course name'] == 'information technology') & (df['year'] == 1),'status'] = "not allowed"

# df.loc[ df['course name'] == 'information technology' & df['year'] == 1,'status'] = "not allowed"  
# ==> 조건문에 여러 조건인 경우 조건마다 () 없는 경우는 Error 발생함 



boolean3 = df['course name'] == 'commerce' 
boolean4 = df['year'] == 4 
df.loc[boolean3 & boolean4,'status'] = "not allowed"

allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

closed_courses = list(course_counts[course_counts < 5].index)
print(closed_courses)

for course in closed_courses:
    df.loc[df["course name"] == course, "status"] = "not allowed"
  
"""
수강 신청이 완료되었습니다. 이제 각 과목을 수강하는 학생수에 따라 크기가 다른 강의실을 배치하려고 합니다.

강의실은 규모에 따라 “Auditorium”, “Large room”, “Medium room”, “Small room” 총 4가지 종류가 있습니다.

아래 조건에 따라 강의실 종류를 지정해 주세요.

80명 이상의 학생이 수강하는 과목은 “Auditorium”에서 진행됩니다.
40명 이상, 80명 미만의 학생이 수강하는 과목은 “Large room”에서 진행됩니다.
15명 이상, 40명 미만의 학생이 수강하는 과목은 “Medium room”에서 진행됩니다.
5명 이상, 15명 미만의 학생이 수강하는 과목은 “Small room”에서 진행됩니다.
폐강 등의 이유로 status가 “not allowed”인 수강생은 room assignment 또한 “not assigned”가 되어야 합니다.
"""

df = pd.read_csv('enrolment_2.csv')

# 과목별 인원 가져오기
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
print(course_counts)

# 각 강의실 규모에 해당되는 과목 리스트 만들기
auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

# not allowed 과목에 대해 값 지정해주기
not_allowed = df["status"] == "not allowed"
df.loc[not_allowed, "room assignment"] = "not assigned"

# allowed 과목에 대해 값 지정해주기
for course in auditorium_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Auditorium"

for course in large_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Large room"
    
for course in medium_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Medium room"
    
for course in small_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Small room"
    
# 정답 출력
print(df)

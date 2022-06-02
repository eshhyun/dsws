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
  


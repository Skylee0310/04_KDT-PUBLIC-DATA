import pandas as pd
import matplotlib.pyplot as plt

# pandas에서 read_csv 함수 호출해서 읽어오기.
weather_df = pd.read_csv('daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)

# 데이터 타입 확인
print(weather_df['날짜'].dtype)

# 컬럼명 변경.
weather_df.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)
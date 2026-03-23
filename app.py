from meteostat import Point
from datetime import datetime
import meteostat
Daily = meteostat.daily.Daily

start = datetime(2020, 1, 1)
end = datetime(2025, 12, 31)

# 使用台中測站 ID（46749）
data = Daily('46749', start, end)
data = data.fetch()

if data is None or data.empty:
    print("❌ 沒有抓到資料")
else:
    print("✅ 成功抓到資料")
    
    cols = ['tavg', 'tmin', 'tmax']
    if 'rhum' in data.columns:
        cols.append('rhum')
    
    data = data[cols]
    print(data.head())
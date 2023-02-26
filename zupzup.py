import FinanceDataReader as fdr
from datetime import datetime, timedelta

# 종목 코드
code = "005930"

# 조회 기간 (1년)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# 주가 데이터 가져오기
df = fdr.DataReader(code, start_date, end_date)

# 결과 출력
print(df)
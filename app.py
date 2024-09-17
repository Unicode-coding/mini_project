import streamlit as st

st.set_page_config(
  page_title="용돈",
  page_icon = "💻"
)

# 함수: 휴대폰 사용 시간을 기반으로 용돈 계산
def calculate_allowance(hours, minutes):
    # 입력받은 시간과 분을 모두 분으로 변환
    total_minutes = hours * 60 + minutes
    # 하루 3시간(180분)에서 사용 시간을 뺌
    remaining_minutes = 180 - total_minutes
    # 남은 시간(분)을 기준으로 용돈 계산
    allowance = remaining_minutes * 40
    return max(0, allowance)

# 함수: 한 달 용돈 계산 (오늘 용돈 * 30일)
def calculate_monthly_allowance(daily_allowance):
    return daily_allowance * 30

# Streamlit UI 구성

# 시간 입력받기 (Streamlit의 time_input 사용)
time_input = st.time_input("오늘 사용한 시간을 입력하세요", value=None)

# 사용한 시간과 분 계산
if time_input:  # 사용자가 시간을 입력한 경우
    hours = time_input.hour  # 입력한 시간
    minutes = time_input.minute  # 입력한 분

    # 용돈 계산 버튼
    
    daily_allowance = calculate_allowance(hours, minutes)
    
    # 오늘의 용돈 결과 출력
    st.success(f"오늘의 용돈은 {daily_allowance}원 입니다.")
    
    # 한 달 용돈 계산
    monthly_allowance = calculate_monthly_allowance(daily_allowance)
    
    # 한 달 용돈 결과 출력
    st.write(f"한 달 예상 용돈은 {monthly_allowance}원 입니다.")


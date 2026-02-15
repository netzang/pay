import streamlit as st
import pandas as pd
from datetime import date

# 웹 페이지 설정
st.set_page_config(page_title="퇴직금 계산기", icon="💰")

st.title("⚖️ 퇴직금 계산기 (웹 버전)")
st.info("입사일과 퇴사일, 최근 3개월 급여를 입력하면 법정 퇴직금을 계산합니다.")

# 입력 구역
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("입사일", date(2023, 1, 1))
    with col2:
        end_date = st.date_input("퇴사일", date.today())

    base_salary = st.number_input("최근 3개월 급여 총액 (원)", value=9000000, step=10000)
    bonus = st.number_input("연간 상여금 총액 (원)", value=0)
    annual_leave = st.number_input("연차수당 (원)", value=0)

# 계산 로직
if st.button("계산하기"):
    # 재직일수 계산
    working_days = (end_date - start_date).days
    
    # 1일 평균임금 계산 공식
    # ((3개월간 임금 총액) + (상여금 x 3/12) + (연차수당 x 3/12)) / 3개월간의 총 일수
    total_wage = base_salary + (bonus * 3/12) + (annual_leave * 3/12)
    avg_daily_wage = total_wage / 90 # 실제로는 해당 월의 일수(89~92일)를 적용하는 것이 정확함
    
    # 퇴직금 산식 적용
    severance_pay = avg_daily_wage * 30 * (working_days / 365)
    
    st.divider()
    st.success(f"### 예상 퇴직금: **{severance_pay:,.0f}원**")
    st.write(f"📍 총 재직일수: {working_days}일")
    st.caption("※ 본 계산은 참고용이며, 정확한 금액은 규정에 따라 차이가 있을 수 있습니다.")
import streamlit as st
import scipy.stats as stats

st.title("🎯 과목별 전략 분석기 (Z점수 & 백분위 자동 계산)")

st.markdown("""
학생부 종합전형 전략 수립을 위한 과목별 상대적 강약 분석 도구입니다.  
점수를 입력하면 Z점수와 백분위를 계산하고, 전략적 문장을 자동으로 생성합니다.
""")

# 사용자 입력 받기
subjects = ["국어", "수학", "영어"]
user_scores = {}
mean_scores = {}
std_devs = {}

st.header("📘 과목별 점수 입력")

for subject in subjects:
    st.subheader(f"{subject}")
    user_scores[subject] = st.number_input(f"{subject} 점수", min_value=0, max_value=100, value=70, key=subject+"_score")
    mean_scores[subject] = st.number_input(f"{subject} 평균 점수", min_value=0.0, max_value=100.0, value=70.0, key=subject+"_mean")
    std_devs[subject] = st.number_input(f"{subject} 표준편차", min_value=1.0, max_value=30.0, value=10.0, key=subject+"_std")

st.markdown("---")

# 결과 분석
st.header("📊 분석 결과")

for subject in subjects:
    z = (user_scores[subject] - mean_scores[subject]) / std_devs[subject]
    percentile = round(stats.norm.cdf(z) * 100, 2)

    if percentile >= 85:
        message = "🎯 **강점 과목입니다. 경쟁력 있는 선택이 가능합니다.**"
    elif percentile >= 60:
        message = "✅ **중상위권입니다. 전략적 활용이 가능합니다.**"
    elif percentile >= 40:
        message = "⚠️ **보통 수준입니다. 약간의 보완이 필요합니다.**"
    else:
        message = "🔻 **하위권입니다. 선택 시 주의가 필요합니다.**"

    st.subheader(f"📘 {subject}")
    st.write(f"- Z점수: `{z:.2f}`")
    st.write(f"- 백분위: `{percentile} %`")
    st.markdown(message)

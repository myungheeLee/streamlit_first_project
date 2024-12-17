import streamlit as st

# MBTI 유형 및 설명 데이터 정의
mbti_descriptions = {
    "INTJ": "INTJ는 전략적 사고와 독립성을 중시하며, 계획을 세우고 이를 실행하는 데 능숙합니다. 이들은 분석적 사고를 통해 복잡한 문제를 해결하는 것을 즐깁니다. 적합한 직업으로는 경영 컨설턴트, 연구원, 데이터 분석가 등이 있습니다.",
    "INFP": "INFP는 창의적이고 공감 능력이 뛰어나며, 가치와 신념을 중시합니다. 예술적 표현과 사람들에게 영감을 주는 일을 즐깁니다. 적합한 직업으로는 작가, 상담사, 예술가 등이 있습니다.",
    "ENTP": "ENTP는 열정적이고 창의적인 문제 해결사로, 새로운 아이디어를 탐구하고 도전하는 것을 즐깁니다. 이들은 혁신적인 프로젝트에 강점을 가지며, 창업가, 마케팅 전문가, 발명가로 적합합니다.",
    # 추가 MBTI 설명을 여기에 추가
}

# Streamlit 애플리케이션
st.title("MBTI 유형에 따른 적합 직업 및 성격")

# MBTI 유형 선택
mbti_type = st.selectbox("당신의 MBTI를 선택하세요:", options=mbti_descriptions.keys())

# 설명 표시
if mbti_type:
    st.subheader(f"{mbti_type} 유형의 특성")
    st.write(mbti_descriptions[mbti_type])

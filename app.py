import streamlit as st

# (2) 함수 (def): 힘(N)과 단면적(mm^2)을 받아 응력(MPa)을 계산하는 함수
def calculate_stress(force, area):
    stress = force / area
    return round(stress, 2)

# 1) 시작 및 앱 제목 설정
st.title("🔩 하중 변화에 따른 소재의 응력 분석 웹")
st.caption("재료공학 진로 연계 프로젝트 | 10931 최성은")
st.divider()

# 2) 리스트 선언: 하중 조건, 소재 이름, 각 소재의 항복 강도(MPa)
loads = [500, 1000, 1500, 2000]
material_names = ["합금 티타늄", "알루미늄(6061-T6)", "스테인리스강(SUS304)", "구리"]
yield_strengths = [1000, 270, 205, 70]  # 직접 조사하여 검증한 각 소재의 항복 강도(MPa)

# 3) 입력 받기 (UI 레이아웃)
st.subheader("1. 실험 조건 설정")

# 소재 선택 (드롭다운 목록)
selected_material = st.selectbox("소재 선택:", material_names)

# 단면적 입력 (슬라이더: 1 ~ 20 mm^2)
area = st.slider("시편의 단면적 입력 (mm²):", min_value=1, max_value=20, value=10)

st.divider()

# 4) 버튼 클릭 시 분석 실행
if st.button("🔍 분석하기", type="primary"):
    # 선택한 소재의 인덱스(위치)를 찾아 해당 소재의 항복 강도 가져오기
    idx = material_names.index(selected_material)
    target_yield = yield_strengths[idx]

    st.subheader("2. 결과 출력 화면")
    st.info(f"- 선택 소재(**{selected_material}**)가 영구 변형될 때의 응력: **{target_yield} MPa**")

    # 표(테이블)로 만들기 위해 결과를 담을 빈 리스트 생성
    result_table = []

    # 6) 반복 출력: for문을 이용해 loads 리스트의 모든 하중 조건 계산
    for force in loads:
        # 함수 호출로 응력 계산
        stress = calculate_stress(force, area)

        # 5) 조건 판단 (if-elif-else)
        if stress < target_yield * 0.7:
            status = "🟢 안전"
        elif stress < target_yield:
            status = "🟡 주의"
        else:
            status = "🔴 항복(영구변형)"

        result_table.append({
            "적용 하중 (N)": force,
            "계산된 응력 (MPa)": stress,
            "판정": status
        })

    # 표 형태로 화면 출력
    st.table(result_table)

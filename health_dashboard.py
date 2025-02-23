import streamlit as st
from crop_health_analyzer import CropHealthAnalyzer, HealthMetrics

def display_health_dashboard():
    st.markdown("<h2 style='color: #2E7D32;'>🌿 Crop Health Dashboard</h2>", unsafe_allow_html=True)
    
    try:
        analyzer = CropHealthAnalyzer()
    except ValueError as e:
        st.error(str(e))
        return

    col1, col2 = st.columns(2)
    with col1:
        soil = st.slider("Soil Health", 0, 100, 70)
        water = st.slider("Water Management", 0, 100, 70)
    with col2:
        pests = st.slider("Pest Control", 0, 100, 70)
        nutrients = st.slider("Nutrient Levels", 0, 100, 70)

    metrics = HealthMetrics(soil, water, pests, nutrients)
    score = analyzer.calculate_overall_score(metrics)
    
    st.markdown(f"""
    <div class='health-score-container score-{analyzer.get_score_status(score).lower()}'>
        <div class='score-number'>{score:.1f}</div>
        <div class='score-status'>{analyzer.get_score_status(score)}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Generating recommendations..."):
        advice, error = analyzer.get_health_recommendations(metrics)
        if advice:
            st.markdown(f"<div class='recommendations-container'>{advice}</div>", unsafe_allow_html=True)
        elif error:
            st.error(error)
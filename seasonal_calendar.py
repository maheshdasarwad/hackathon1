import streamlit as st
from calendar_data import SEASONS, get_current_season

def display_seasonal_calendar():
    st.markdown("<h2 style='color: #2E7D32;'>🗓️ Seasonal Farming Calendar</h2>", unsafe_allow_html=True)
    
    current_season = get_current_season()
    selected_season = st.selectbox(
        "Select season:",
        list(SEASONS.keys()),
        index=list(SEASONS.keys()).index(current_season.name)
    )
    
    season_data = SEASONS[selected_season]
    
    st.markdown(f"""
    <div class='season-card'>
        <h3>{season_data.name} Season</h3>
        <p>{season_data.description}</p>
        <h4>🌱 Recommended Crops</h4>
        <ul class='crop-list'>
            {''.join(f'<li>{crop}</li>' for crop in season_data.recommended_crops)}
        </ul>
    </div>
    """, unsafe_allow_html=True)
import streamlit as st
from crop_advisor import CropAdvisor
from seasonal_calendar import display_seasonal_calendar
from health_dashboard import display_health_dashboard
from dotenv import load_dotenv

import os

load_dotenv()
print("API Key:", os.getenv("GOOGLE_API_KEY"))  # Should show your key

# Inject Header HTML
def inject_header():
    header = """
    <header>
        <div class="header-content">
            <div class="logo">
                <span>🍃 𝐒𝐦𝐚𝐫𝐭 𝐅𝐚𝐫𝐦 𝐌𝐚𝐧𝐚𝐠𝐞𝐫</span>
                <img class="home" src="https://cdn-icons-png.flaticon.com/512/25/25694.png" alt="home" width="30">
            </div>
            <div class="user-actions">
                <span>𝗪𝗲𝗹𝗰𝗼𝗺𝗲</span>
                <button>Logout</button>
            </div>
        </div>
    </header>
    """
    st.markdown(header, unsafe_allow_html=True)

# Inject Footer HTML
def inject_footer():
    footer = """
    <footer>
        <div class="footer-content">
            <p><b>© 2024 Smart Farm Manager. All rights reserved.</b></p>
            <div class="footer-links">
                <a href="#"><b>About</b></a>
                <a href="#"><b>Contact</b></a>
                <a href="#"><b>Privacy</b></a>
                <span><b>Created by Team AgniDev</b></span>
            </div>
        </div>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Farmer's Crop Planning Assistant",
        page_icon="🌾",
        layout="wide"
    )

    # Load custom CSS
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='main-header'>🌾 Farmer's Crop Planning Assistant</h1>", unsafe_allow_html=True)

    # Create tabs for different features
    tab1, tab2, tab3 = st.tabs(["Crop Advisor", "Seasonal Calendar", "Health Dashboard"])

    with tab1:
        display_crop_advisor()

    with tab2:
        display_seasonal_calendar()

    with tab3:
        display_health_dashboard()

def display_crop_advisor():
    # Instructions
    st.markdown(
        """
        <div class='instruction-text'>
            <b>How to use this tool:</b>
            <ol>
                <li>Enter the name of your crop in the input field below</li>
                <li>Click on 'Get Advice' to receive detailed planning information</li>
                <li>The system will provide you with specific guidance for:</li>
                <ul>
                    <li>Ploughing</li>
                    <li>Sowing</li>
                    <li>Watering</li>
                    <li>Fertilization</li>
                    <li>Harvesting</li>
                </ul>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create input section
    st.markdown("<div class='crop-input'>", unsafe_allow_html=True)
    crop_name = st.text_input("Enter your crop name:", placeholder="e.g., Rice, Wheat, Cotton")
    submit_button = st.button("Get Advice")
    st.markdown("</div>", unsafe_allow_html=True)

    # Initialize CropAdvisor
    try:
        advisor = CropAdvisor()
    except ValueError as e:
        st.error(str(e))
        return

    if submit_button and crop_name:
        try:
            with st.spinner('Getting expert advice for your crop...'):
                response, error = advisor.get_crop_advice(crop_name)

                if response:
                    st.markdown("<div class='response-container'>", unsafe_allow_html=True)
                    st.markdown("### 📋 Crop Planning Advice")
                    st.markdown(response)
                    st.markdown("</div>", unsafe_allow_html=True)
                elif error:
                    st.error(error)
                else:
                    st.error("Unable to get advice at the moment. Please try again.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
    elif submit_button:
        st.warning("Please enter a crop name first.")

if __name__ == "__main__":
    main()
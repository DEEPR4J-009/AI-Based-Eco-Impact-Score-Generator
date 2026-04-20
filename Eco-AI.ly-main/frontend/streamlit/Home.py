import streamlit as st
import os

# Set up the page configuration
st.set_page_config(
    page_title="Eco AI.ly - Sustainable Predictions",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Consolidated CSS for better styling
st.markdown(
    """
    <style>
    .main-header { font-size: 2.5rem; color: #2E7D32; text-align: center; margin-bottom: 1rem; }
    .sub-header { font-size: 1.8rem; color: #1B5E20; margin-top: 2rem; margin-bottom: 1rem; }
    .feature-card { padding: 1.5rem; margin: 1rem 0; }
    .feature-title { color: #2E7D32; }
    .cta-section { text-align: center; margin: 2rem 0; }
    .footer { text-align: center; margin-top: 3rem; padding: 1rem; border-top: 1px solid #E0E0E0; }
    .credits { text-align: center; margin-top: 1rem; padding: 1rem; background-color: #f1f8e9; border-radius: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Display the logo
col1, col2, col3 = st.columns([0.5, 3, 0.5])
with col2:
    HERE = os.path.dirname(__file__)
    logo_path = os.path.join(HERE, "assets", "images", "logo.png")
    st.image(logo_path, width=1600)

# Consolidated content sections
content = """
    <div class="feature-card">
        <h3 class="feature-title">🌱 Welcome to Eco AI.ly</h3>
        <p>Your innovative platform at the intersection of <strong>Artificial Intelligence</strong> 🤖 and <strong>Sustainability</strong> 🌍. 
        We empower decision-makers with accurate, real-time predictions on environmental metrics, enabling a greener future for all.</p>
    </div>

    <h2 class="sub-header">✨ Our Key Features</h2>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
        <div class="feature-card">
            <h3 class="feature-title">📊 Predictive Analytics</h3>
            <p>• 📈 Real-time energy consumption forecasts<br>
               • 🌡️ Environmental impact predictions<br>
               • 📉 Trend analysis and pattern recognition</p>
        </div>
        <div class="feature-card">
            <h3 class="feature-title">📱 Data Visualization</h3>
            <p>• 📊 Interactive dashboards<br>
               • 📈 Dynamic charts and graphs<br>
               • 🎯 Customizable data views</p>
        </div>
        <div class="feature-card">
            <h3 class="feature-title">🤖 AI-Powered Insights</h3>
            <p>• 🧠 Machine learning models<br>
               • 🔍 Pattern recognition<br>
               • 📋 Automated reporting</p>
        </div>
    </div>

    <h2 class="sub-header">🌍 Explore Our Platform</h2>
    <div class="feature-card">
        <h3 class="feature-title">🇮🇳 India Data Dashboard</h3>
        <p>• 📊 Comprehensive energy consumption metrics<br>
           • ⚡ Real-time data updates<br>
           • 📈 Historical trend analysis<br>
           • 🔄 Export and import statistics</p>
    </div>

    <h2 class="sub-header">⚙️ Our Technology Stack</h2>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
        <div class="feature-card">
            <h3 class="feature-title">🔧 Backend Technologies</h3>
            <p>• 🐍 Python & TensorFlow for AI models<br>
               • 🔄 Advanced data processing pipelines<br>
               • ⚡ Real-time data integration</p>
        </div>
        <div class="feature-card">
            <h3 class="feature-title">🎨 Frontend Technologies</h3>
            <p>• 📱 Streamlit for interactive dashboards<br>
               • 📊 Modern visualization libraries<br>
               • 📱 Responsive design</p>
        </div>
    </div>

    <div class="cta-section">
        <h2 class="feature-title">🌟 Ready to Make a Difference?</h2>
        <p>Join us in our mission to create a sustainable future through AI-powered insights. 🌱</p>
    </div>

    <div class="credits">
        <h3 style="color: #2E7D32;">👨‍💻 Created By</h3>
        <p><strong>Deepraj Patel</strong> — 22BCS14957</p>
        <p><strong>Harman Singh</strong> — 22BCS14957</p>
    </div>

    <div class="footer">
        <p>© 2024 Eco AI.ly - Empowering Sustainable Decisions with AI 🌿</p>
    </div>
"""

# Render all content at once
st.markdown(content, unsafe_allow_html=True)
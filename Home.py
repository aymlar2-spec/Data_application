import streamlit as st

st.markdown("""
<div style='text-align:center; padding:30px;'>
    <h1>📱 Google Play App Analytics</h1>
    <h3>Application Discovery & Insights Dashboard</h3>
    <p>
        Search for applications available on the Google Play Store,
        explore ratings and categories, and visualize search results
        through interactive dashboards.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Platform", "Google Play")

with col2:
    st.metric("Search Engine", "Live API")

with col3:
    st.metric("Analytics", "Interactive")

st.markdown("---")

st.info(
    "👈 Use the navigation menu on the left to search for applications and explore analytics dashboards."
)
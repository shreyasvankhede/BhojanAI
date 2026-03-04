import streamlit as st

def render_navbar():
    st.write("")
    logged_in = st.session_state.get("logged_in", False)
    if logged_in:
     Name = st.session_state.get("Name")
    else:
       Name=None
    
    col1, col2, col3, col4 = st.columns([4, 1, 1, 1])

    with col1:
        st.markdown("## 🍽BhojanAI")
        if Name:
            st.caption(f"Welcome {Name[0]} 👋")

    with col2:
        if logged_in:
         if st.button("Log Food"):
            st.switch_page("pages/Food_Detection.py")

    with col3:
        if logged_in:
         if st.button("Reports"):
            st.switch_page("pages/report.py")

    with col4:
        if logged_in:
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.session_state.Name = None
                st.switch_page("front.py")
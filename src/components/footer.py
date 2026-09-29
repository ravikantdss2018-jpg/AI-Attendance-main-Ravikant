import streamlit as st

def footer_home():
    file_id = "1RgNuW5zDSfvZQhN_GrSHIKKnybWC1-Rx"

    logo_url = (f"https://i.ibb.co/fGy70fXD/R-K-Logic-Loop-Logo.png &sz=w500")
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center"> 
            <p style="font-weight:bold; color:white;"> Created with 💖 by Ravikant Chaudhary</p>
            <img src = '{logo_url}' style= 'max-height:25px' max-width:200px />
        </div>       
                """, unsafe_allow_html=True)


def footer_dashbord():
    #file_id = "1RgNuW5zDSfvZQhN_GrSHIKKnybWC1-Rx"

    logo_url = (f"https://i.ibb.co/fGy70fXD/R-K-Logic-Loop-Logo.png &sz=w500")
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center"> 
            <p style="font-weight:bold; color:black;"> Created with 💖 by Ravikant Chaudhary</p>
            <img src = '{logo_url}' style= 'max-height:25px' max-width:200px />
        </div>       
                """, unsafe_allow_html=True)
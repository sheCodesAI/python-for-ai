import streamlit as st
import pandas as pd

name = st.text_input("Enter your Name")
fname = st.text_input("Enter your Father Name")
sname = st.text_input("Enter your Surname")

adr = st.text_area("Enter your Address")

classdata = st.selectbox(
    "Enter your Grade:",
    (1, 2, 3, 4, 5)
)

button = st.button("Done")

if button:
    st.success("Form Submitted Successfully!")

    st.markdown(f"""
    **Name:** {name}

    **Father Name:** {fname}

    **Surname:** {sname}

    **Address:** {adr}

    **Class:** {classdata}
    """)

    **Class:** {classdata}
    """)

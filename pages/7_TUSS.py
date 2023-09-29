import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from modules.qmod import show_pdf_2


st.set_page_config(
    page_title="TUSS",
    page_icon="🐓",
    layout="wide",
    initial_sidebar_state="auto",
)


def main():
    authenticator.logout("Logout", "sidebar")

    st.title('Tabela TUSS')

    if st.button("Tabela Completa"):
        filename = "src/TABELA TUSS.pdf"
        show_pdf_2(filename)


if __name__ == "__main__":
    # Create an instance of the Authenticate class
    authenticator = stauth.Authenticate(
        dict(st.secrets['credentials']),
        st.secrets['cookie']['name'],
        st.secrets['cookie']['key'],
        st.secrets['cookie']['expiry_days'],
        st.secrets['preauthorized']
    )

    name, authentication_status, username = authenticator.login(
        "Login", "main")
    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        main()

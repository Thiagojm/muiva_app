import streamlit as st
import streamlit_authenticator as stauth
import qmod as qm


def main():
    # Create or get the session state
    if "session" not in st.session_state:
        st.session_state.session = qm.SessionState()
        
    # Cria o menu suspenso na barra lateral com as opções e as tabelas em ordem
    st.sidebar.markdown(f"Bem vinda {name}!")
    authenticator.logout("Logout", "sidebar")

        
            

    ####### Pagina principal #######

    ####### IMC #######

    # Header
    st.header("Página Dra. Monyque Cunha Trindade")
    st.divider()
    
    st.image("src/outros/muiva.jpg", caption="Muivinha Linda")
    
if __name__ == "__main__":
    # Create an instance of the Authenticate class
    authenticator = stauth.Authenticate(
    dict(st.secrets['credentials']),
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days'],
    st.secrets['preauthorized']
)
    table_pass = st.secrets['table_pass']["pass"]
    
    name, authentication_status, username = authenticator.login("Login", "main")
    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        main()
    

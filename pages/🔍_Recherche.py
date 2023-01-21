import streamlit as st
import pandas as pd

musique_4sites=pd.read_csv(r'C:\Users\moi\webscrapping\resultat_4_sites_clean.csv')
df_france = musique_4sites[musique_4sites['Region'] == 'france']
df_monde = musique_4sites[musique_4sites['Region'] == 'monde']


artiste_a_chercher = None
df=None

st.set_page_config(
    page_title="Recherche"
)
st.title("Recherche 🔍")

option = st.selectbox("**Type de données :**", ('Artiste', 'Titre'))

choix_region = st.radio("**Region :**", ('France', 'Monde','Tout'))
   
if choix_region == 'France':
    df = df_france
elif choix_region == 'Monde':
    df = df_monde
else:
    df = musique_4sites
if option == 'Artiste':
    options = df['Artiste'].unique()
elif option == 'Titre':
    options = df['Titre'].unique()

with st.form("Veuillez choisir "):

    a_chercher = st.selectbox("**Choix :**", options)

    submitted=st.form_submit_button("Afficher")

    if submitted:
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
         
        if option=='Artiste':
          
                df_artiste= df[df['Artiste']==a_chercher]
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                st.table(df_artiste.drop(['Image','Avis'], axis=1))  
                st.empty()

        if option=='Titre':
            df_titre= df[df['Titre']==a_chercher]
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(df_titre.drop(['Image','Avis'], axis=1))  
            st.empty()
import streamlit as st
import pandas as pd

musique_4sites=pd.read_csv(r'C:\Users\moi\webscrapping\resultat_4_sites_clean.csv')
df_france = musique_4sites[musique_4sites['Region'] == 'france']
df_monde = musique_4sites[musique_4sites['Region'] == 'monde']


st.set_page_config(
    page_title="Comparaisons"
)
st.title("Comparaisons 👀")

with st.form("Veuillez choisir "):
    choix_region = st.radio("**Region :**", ('France', 'Monde','France & Monde'), index=0)
    submitted=st.form_submit_button("Afficher")

    if submitted:
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
        """
        
        if choix_region =="France":
            st.warning("Ici, (counts = 1) indique qu'un titre est présent dans les deux classements, tandis que (counts = 2) indique qu'un titre est présent dans les deux classements deux fois, cela peut notamment s'expliquer par des remix de la chanson (noté dans les classements comme deux musiques différentes donc pouvant apparaitre 2 fois dans le même classement")
            
            st.markdown("""Titres qui sont a la fois dans le top 100 des musiques les plus écoutées et également les plus téléchargées""")
          
            df_snep = df_france[df_france['Site'] == 'snep']
            df_amazon_fr = df_france[df_france['Site'] == 'amazon_fr']
            titre_join_france = pd.merge(df_snep, df_amazon_fr, on=['Titre', 'Artiste'])
            titre_join_france = titre_join_france.groupby(['Titre', 'Artiste']).size().reset_index(name='counts')
            titre_join_france = titre_join_france.sort_values(by='counts', ascending=False)
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(titre_join_france)
            st.empty()

            st.markdown("""Artistes qui sont a la fois dans le top 100 des musiques les plus écoutées et également les plus téléchargées""")
            artiste_join_france = pd.merge(df_snep, df_amazon_fr, on=['Artiste'])
            artiste_join_france = artiste_join_france.groupby(['Artiste']).size().reset_index(name='counts')
            artiste_join_france = artiste_join_france.sort_values(by='counts', ascending=False)
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(artiste_join_france) 
            st.empty()
         
            

        if choix_region=="Monde":
            st.warning("Ici, (counts = 1) indique qu'un titre est présent dans les deux classements, tandis que (counts = 2) indique qu'un titre est présent dans les deux classements deux fois, cela peut notamment s'expliquer par des remix de la chanson (noté dans les classements comme deux musiques différentes donc pouvant apparaitre 2 fois dans le même classement")
           
            st.markdown("""Titres qui sont a la fois dans le top 100 des musiques les plus écoutées et également les plus téléchargées""")

            df_billboard = df_monde[df_monde['Site'] == 'billboard']
            df_amazon_com = df_monde[df_monde['Site'] == 'amazon_com']
            titre_join_monde = pd.merge(df_billboard, df_amazon_com, on=['Titre', 'Artiste'])
            titre_join_monde = titre_join_monde.groupby(['Titre', 'Artiste']).size().reset_index(name='counts')
            titre_join_monde = titre_join_monde.sort_values(by='counts', ascending=False)
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(titre_join_monde)
            st.empty()

            st.markdown("""Artistes qui sont a la fois dans le top 100 des musiques les plus écoutées et également les plus téléchargées""")
            artiste_join_monde = pd.merge(df_billboard, df_amazon_com, on=['Artiste'])
            artiste_join_monde = artiste_join_monde.groupby(['Artiste']).size().reset_index(name='counts')
            artiste_join_monde = artiste_join_monde.sort_values(by='counts', ascending=False)
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(artiste_join_monde)
            st.empty()

        if choix_region=='France & Monde':
            st.markdown("""Titres qui sont a la fois dans les top 100 des musiques les plus écoutées ou les plus téléchargées à la fois en France et dans le monde""")
    
            titre_join_france_monde = pd.merge(df_france, df_monde, on=['Titre', 'Artiste'])
            titre_join_france_monde = titre_join_france_monde['Titre'].unique()
            titre_join_france_monde = pd.DataFrame({'Titre': titre_join_france_monde})
            
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(titre_join_france_monde['Titre'])
            st.empty()

            st.markdown("""Artistes qui sont a la fois dans les top 100 des musiques les plus écoutées ou les plus téléchargées à la fois en France et dans le monde""")
            artiste_join_france_monde = pd.merge(df_france, df_monde, on=['Artiste'])
            artiste_join_france_monde = artiste_join_france_monde['Artiste'].unique()
            artiste_join_france_monde = pd.DataFrame({'Artiste': artiste_join_france_monde})
            
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(artiste_join_france_monde['Artiste'])
            
            
            



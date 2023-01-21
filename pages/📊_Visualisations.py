import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


musique_france = pd.read_csv(r'C:\Users\moi\webscrapping\genre_france.csv')
musique_monde = pd.read_csv(r'C:\Users\moi\webscrapping\genre_monde.csv')

musique_4sites=pd.read_csv(r'C:\Users\moi\webscrapping\resultat_4_sites_clean.csv')
df_france = musique_4sites[musique_4sites['Region'] == 'france']
df_monde = musique_4sites[musique_4sites['Region'] == 'monde']


image_artistes_top_france = Image.open('artistes_top_france.jpg')
image_artistes_top_monde = Image.open('artistes_top_monde.jpg')


st.set_page_config(
    page_title="Visualisations"
)
st.title("Visualisations 📊")

st.header(f"Analyse des données")
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.form("Veuillez choisir "):
    option = st.selectbox("**Type de données :**", ('Genre de musique', 'Top'))

    choix_region = st.radio(
        "**Region :**", ['France', 'Monde', 'France vs Monde'], index=0)
    submitted = st.form_submit_button("Afficher")

    if submitted:
        hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
        if option == 'Genre de musique':

            def my_autopct(pct):
                if pct > 3:
                    return '%1.1f%%' % pct
                else:
                    return ''
            if choix_region == 'France':
                plt.pie(musique_france.Genre.value_counts(),
                        colors=sns.color_palette('muted'), autopct=my_autopct)
                plt.legend(musique_france.Genre.value_counts().index,
                           title="Genre", bbox_to_anchor=(1, 0, 0.5, 1))
                plt.title("Répartition des genres en France")
                st.pyplot()

                st.empty()
                st.empty()

                plot = sns.countplot(
                    y="Genre", data=musique_france, palette='muted')
                for p in plot.patches:
                    plot.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + 0.5), va='center', size=10)

                plt.title("Nombres de titres par genre en France")
                st.pyplot()

            if choix_region == 'Monde':
                plt.pie(musique_monde.Genre.value_counts(),
                        colors=sns.color_palette('muted'), autopct=my_autopct)
                plt.legend(musique_monde.Genre.value_counts().index,
                           title="Genre", bbox_to_anchor=(1, 0, 0.5, 1))
                plt.title("Répartition des genres dans le monde")
                st.pyplot()

                st.empty()
                st.empty()

                plot = sns.countplot(
                    y="Genre", data=musique_monde, palette='muted')
                for p in plot.patches:
                    plot.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + 0.5), va='center', size=10)

                plt.title("Nombres de titres par genre dans le monde")
                st.pyplot()

            if choix_region == 'France vs Monde':
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 12))

                ax1.pie(musique_monde.Genre.value_counts(),
                        colors=sns.color_palette('muted'), autopct=my_autopct)
                ax1.legend(musique_monde.Genre.value_counts().index,
                           title="Genre", bbox_to_anchor=(0, 0, 0, 1))
                ax1.set_title("Répartition des genres dans le monde")

                ax2.pie(musique_france.Genre.value_counts(),
                        colors=sns.color_palette('muted'), autopct=my_autopct)
                ax2.legend(musique_france.Genre.value_counts().index,
                           title="Genre", bbox_to_anchor=(1, 0, 0.5, 1))
                ax2.set_title("Répartition des genres en France")

                st.pyplot()

                st.empty()

                fig, ax = plt.subplots(figsize=(14, 6))
                df_combined = pd.concat([musique_monde, musique_france])

                plot=sns.countplot(y="Genre", hue='Region', data=df_combined)
                plt.title("Nombres de titres par genre dans le monde et en France")
                st.pyplot()

        if option == 'Top':
            if choix_region == 'France':
                st.markdown("""Voici les 10 premières musiques parmi le top 100 des musiques les plus écoutées en France""")
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                st.table(df_france[df_france['Site'] == 'snep'].drop(['Image','Avis','Region','Site'], axis=1)[:10])
                st.empty()
                
                st.markdown("""Voici les 10 premières musiques parmi le top 100 des musiques les plus téléchargées en France""")
                st.table(df_france[df_france['Site'] == 'amazon_fr'].drop(['Image','Region','Site'], axis=1)[:10])
                st.empty()
                
                st.markdown("""---""")
                st.image(image_artistes_top_france, use_column_width=True, clamp=True)
                st.markdown("""---""")
                
                counts = df_france['Titre'].value_counts()[:20]
                counts = counts.sort_values(ascending=True)
                counts.plot(kind='barh',color = sns.color_palette('muted'))
                plt.xticks(range(0, 4, 1))
                plt.ylabel('Titres')
                plt.xlabel('Nombre de fois dans le top')
                st.pyplot()

                st.empty()

                counts = df_france['Artiste'].value_counts()[:20]
                counts = counts.sort_values(ascending=True)
                counts.plot(kind='barh',color = sns.color_palette('muted'))
                plt.xticks(range(0, 8, 1))
                plt.ylabel('Artistes')
                plt.xlabel('Nombre de fois dans le top')
                st.pyplot()

            if choix_region == 'Monde':
                st.markdown("""Voici les 10 premières musiques parmi le top 100 des musiques les plus écoutées dans le monde""")
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                st.table(df_monde[df_monde['Site'] == 'billboard'].drop(['Image','Avis','Region','Site'], axis=1)[:10])
                st.empty()
                
                
                st.markdown("""Voici les 10 premières musiques parmi le top 100 des musiques les plus téléchargées dans le monde""")
                st.table(df_monde[df_monde['Site'] == 'amazon_com'].drop(['Image','Region','Site'], axis=1)[:10])
                st.empty()

                st.markdown("""---""")
                st.image(image_artistes_top_monde, use_column_width=True, clamp=True)
                st.markdown("""---""")

                counts = df_monde['Titre'].value_counts()[:20]
                counts = counts.sort_values(ascending=True)
                counts.plot(kind='barh',color = sns.color_palette('muted'))
                plt.xticks(range(0, 4, 1))
                # Add labels and show the plot
                plt.ylabel('Titres')
                plt.xlabel('Nombre de fois dans le top')
                st.pyplot()

                st.empty()

                counts = df_monde['Artiste'].value_counts()[:20]
                counts = counts.sort_values(ascending=True)
                counts.plot(kind='barh',color = sns.color_palette('muted'))
                plt.xticks(range(0, 21, 1))
                plt.ylabel('Artistes')
                plt.xlabel('Nombre de fois dans le top')
                st.pyplot()

            if choix_region == 'France vs Monde':
                st.markdown("""Voici les 10 premières musiques parmi le top 100 des musiques les plus écoutées en France vs dans le monde """)
                titre_ecoute = pd.merge(df_france[df_france['Site'] == 'snep'].drop(['Image','Avis','Region','Site'], axis=1), df_monde[df_monde['Site'] == 'billboard'].drop(['Image','Avis','Region','Site'], axis=1), on=['Classement'])
                titre_ecoute.columns=['Classement','Titre_Top_France','Artiste_Top_France','Titre_Top_Monde','Artiste_Top_Monde']
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                st.table(titre_ecoute[:10])
                st.empty()
                
                st.markdown("""Voici les 10 premières musiques parmi le top 100 des musiques les plus achetées sur Amazon Music en France vs dans le monde """)
                titre_ecoute = pd.merge(df_france[df_france['Site'] == 'amazon_fr'].drop(['Image','Avis','Region','Site'], axis=1), df_monde[df_monde['Site'] == 'amazon_com'].drop(['Image','Avis','Region','Site'], axis=1), on=['Classement'])
                titre_ecoute.columns=['Classement','Titre_Top_France','Artiste_Top_France','Titre_Top_Monde','Artiste_Top_Monde']
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                st.table(titre_ecoute[:10])
                st.empty()

                st.markdown("""---""")
                st.image(image_artistes_top_france, use_column_width=True, clamp=True)
                st.empty()
                st.image(image_artistes_top_monde, use_column_width=True, clamp=True)
                st.empty()
                st.markdown("""---""")

                st.markdown("""Voici les 20 titres les plus ecoutés et téléchargés en France vs dans le monde """)
                fig, (ax1, ax2) = plt.subplots(2,1, figsize=(14, 12))
                
                counts1 = df_france['Titre'].value_counts()[:20]
                counts1 = counts1.sort_values(ascending=True)
                counts1.plot(kind='barh',color = sns.color_palette('muted'), ax=ax1)
                ax1.set_xticks(range(0, 4, 1))
                ax1.set_ylabel('Titres')
                ax1.set_xlabel('Nombre de fois dans le top')

                counts2 = df_monde['Titre'].value_counts()[:20]
                counts2 = counts2.sort_values(ascending=True)
                counts2.plot(kind='barh',color = sns.color_palette('muted'), ax=ax2)
                ax2.set_xticks(range(0, 4, 1))
                ax2.set_ylabel('Titres')
                ax2.set_xlabel('Nombre de fois dans le top')
                
                st.pyplot()
                st.empty()

                st.markdown("""Voici les 20 artistes les plus ecoutés et téléchargés en France vs dans le monde """)
                fig, (ax1, ax2) = plt.subplots(2,1, figsize=(14, 12))
                
                counts1 = df_france['Artiste'].value_counts()[:20]
                counts1 = counts1.sort_values(ascending=True)
                counts1.plot(kind='barh',color = sns.color_palette('muted'),ax=ax1)
                ax1.set_xticks(range(0, 8, 1))
                ax1.set_ylabel('Artistes')
                ax1.set_xlabel('Nombre de fois dans le top')
                
                counts2 = df_monde['Artiste'].value_counts()[:20]
                counts2= counts2.sort_values(ascending=True)
                counts2.plot(kind='barh',color = sns.color_palette('muted'), ax=ax2)
                ax2.set_xticks(range(0, 21, 1))
                ax2.set_ylabel('Artistes')
                ax2.set_xlabel('Nombre de fois dans le top')
                st.pyplot()
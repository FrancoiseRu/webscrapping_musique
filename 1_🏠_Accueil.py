import streamlit as st
from PIL import Image


image_3sites = Image.open('3sites.jpg')


st.set_page_config(
    page_title="Musique"
)

st.title("♪ Notre projet ♪")
st.header("Chanelle WEA et Françoise RUCH")
st.markdown(
    """
Analyse des titres musicaux les plus écoutés et les titres les plus vendus en France et dans le monde en 2021.

Nous avons scrapper les 4 pages : SNEP, Amazon France, Billboard et Amazon Monde
"""
)
st.empty()
st.image(image_3sites)

st.markdown(
    """
---

### Listes des 4 sites utilisés: 

- **Top 100 des musiques les plus écoutés:**

    - en France : **SNEP**
    Le Syndicat national de l'édition phonographique est une association interprofessionnelle qui défend les intérêts de l'industrie française du disque phonographique depuis 1922. 

    - dans le monde : **Billboard**
    Billboard est un magazine hebdomadaire américain consacré à l'industrie du disque

- **Top 100 des musiques les plus téléchargés:**

    Nous avons choisi le site Amazon Music, qui est une plateforme de streaming de musique et un magasin de musique en ligne exploité par Amazon.

    - en France : **Amazon France**

    - dans le monde : **Amazon Monde**

---

### Lien de tous les sites

"""

)

with st.expander("Liens"):
    st.markdown(
        "   - [Amazon France](https://www.amazon.fr/gp/bestsellers/2021/dmusic/digital-music-track/ref=zg_bsar_pg_1/ref=zg_bsar_pg_1?ie=UTF8&pg=1) ")
    st.markdown(
        "   - [SNEP](https://snepmusique.com/les-tops/le-top-de-lannee/top-singles-annee/?annee=2021) ")
    st.markdown(
        "   - [Amazon Monde](https://www.amazon.com/gp/bestsellers/2021/dmusic/digital-music-track/ref=zg_bsar_cal_ye) ")
    st.markdown(
        "   - [Billboard](https://www.billboard.com/charts/year-end/2021/billboard-global-200/) ")

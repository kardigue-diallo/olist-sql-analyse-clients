import base64
import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Olist E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)


# Fonction pour appliquer une image de fond personnalisée
def set_bg_image(image_url):
  st.markdown(
      f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        /* Ajout d'un fond semi-transparent blanc/clair sur le contenu principal pour garder une excellente lisibilité des textes et graphiques */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.92);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        </style>
        """,
      unsafe_allow_html=True,
  )


# Remplacez le lien ci-dessous par l'URL de votre image (ou un lien vers une image hébergée)
set_bg_image(
    "https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=1920&auto=format&fit=crop"
)

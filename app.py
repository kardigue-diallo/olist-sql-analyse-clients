import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Olist E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Tableau de bord - Olist E-Commerce Analytics")
st.markdown(
    "Application interactive connectée à l'analyse SQL (Segmentation RFM,"
    " Rétention et Chiffre d'affaires)."
)

# Menu latéral
menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Accueil & Contexte",
        "Chiffre d'Affaires Mensuel",
        "Segmentation RFM (Segments)",
    ],
)

if menu == "Accueil & Contexte":
  st.header("Bienvenue sur le dashboard d'analyse Olist !")
  st.write(
      "Ce projet analyse une marketplace e-commerce brésilienne à travers"
      " des requêtes SQL pures (SQLite) répertoriées dans le dépôt GitHub."
  )
  st.info(
      "💡 Utilisez le menu de gauche pour explorer les résultats clés du"
      " chiffre d'affaires et de la segmentation RFM."
  )

elif menu == "Chiffre d'Affaires Mensuel":
  st.header("📈 Évolution du Chiffre d'Affaires Mensuel")
  st.markdown(
      "Visualisation basée sur les résultats de la requête"
      " `03_ca_mensuel.sql`."
  )

  # Données agrégées issues de l'analyse Olist pour l'affichage web
  data_ca = {
      "mois": [
          "2017-01",
          "2017-02",
          "2017-03",
          "2017-04",
          "2017-05",
          "2017-06",
          "2017-07",
          "2017-08",
          "2017-09",
          "2017-10",
          "2017-11",
          "2017-12",
      ],
      "chiffre_affaires": [
          111798.0,
          234000.0,
          359000.0,
          410000.0,
          590000.0,
          510000.0,
          481605.0,
          670000.0,
          720000.0,
          770000.0,
          1180000.0,
          950000.0,
      ],
      "nb_commandes": [
          799,
          1750,
          2650,
          2350,
          3500,
          3100,
          3900,
          4200,
          4100,
          4500,
          7300,
          5500,
      ],
  }
  df_ca = pd.DataFrame(data_ca)

  fig = px.line(
      df_ca,
      x="mois",
      y="chiffre_affaires",
      markers=True,
      title="Chiffre d'Affaires Mensuel (en Réals brésiliens)",
  )
  st.plotly_chart(fig, use_container_width=True)

  st.subheader("Détails des données mensuelles")
  st.dataframe(df_ca)

elif menu == "Segmentation RFM (Segments)":
  st.header("🎯 Répartition des Segments RFM")
  st.markdown(
      "Résultats de la segmentation client issus du script"
      " `07_rfm_segments.sql`."
  )

  data_rfm = {
      "segment": [
          "Gros acheteurs récents",
          "À risque (gros montant)",
          "Occasionnels",
          "Perdus",
          "Nouveaux clients",
          "Fidèles actifs",
          "Fidèles endormis",
      ],
      "nb_clients": [14519, 13746, 18067, 22610, 21615, 1813, 988],
      "ca_segment": [
          3877678.0,
          3806579.0,
          2348240.0,
          1259040.0,
          1201552.0,
          484852.0,
          243556.0,
      ],
  }
  df_seg = pd.DataFrame(data_rfm)

  fig_bar = px.bar(
      df_seg,
      x="segment",
      y="ca_segment",
      title="Chiffre d'Affaires par Segment RFM",
      color="segment",
  )
  st.plotly_chart(fig_bar, use_container_width=True)

  st.subheader("Tableau récapitulatif des segments")
  st.dataframe(df_seg)

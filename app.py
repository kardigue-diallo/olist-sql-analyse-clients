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
    "Application interactive mettant en valeur l'analyse SQL complète d'une"
    " marketplace (9 tables, Segmentation RFM, Cohortes et Chiffre d'affaires)."
)

# Menu latéral enrichi
menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Accueil & Contexte",
        "Chiffre d'Affaires Mensuel",
        "Segmentation RFM (Segments)",
        "Rétention par Cohortes",
        "Statuts des Commandes",
    ],
)

if menu == "Accueil & Contexte":
  st.header("Bienvenue sur le dashboard d'analyse Olist !")
  st.write(
      "Ce projet analyse une marketplace e-commerce brésilienne à travers"
      " un ensemble de scripts SQL pures (SQLite) exploitant 9 tables de"
      " données distinctes."
  )

  st.markdown("### 📁 Les 9 tables du projet :")
  st.markdown("""
    - `olist_orders_dataset` (Commandes)
    - `olist_customers_dataset` (Clients et correspondance `customer_unique_id`)
    - `olist_order_items_dataset` (Lignes de commande / articles)
    - `olist_order_payments_dataset` (Paiements)
    - `olist_order_reviews_dataset` (Avis clients)
    - `olist_products_dataset` (Produits)
    - `olist_sellers_dataset` (Vendeurs)
    - `olist_geolocation_dataset` (Géolocalisation)
    - `product_category_name_translation` (Traduction des catégories)
    """)

elif menu == "Chiffre d'Affaires Mensuel":
  st.header("📈 Évolution du Chiffre d'Affaires Mensuel")
  st.markdown("Basé sur les scripts `03_ca_mensuel.sql` et `09_croissance_mensuelle.sql`.")

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
  st.dataframe(df_ca)

elif menu == "Segmentation RFM (Segments)":
  st.header("🎯 Segmentation RFM des Clients")
  st.markdown("Basé sur le script `07_rfm_segments.sql`.")

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
  st.dataframe(df_seg)

elif menu == "Rétention par Cohortes":
  st.header("🔄 Analyse de Rétention par Cohortes Mensuelles")
  st.markdown(
      "Basé sur l'optimisation réalisée dans `08_cohortes_retention.sql`"
      " (mesure du taux de rachat des clients à M1, M3, M6)."
  )

  # Données de synthèse issues de l'analyse
  data_cohortes = {
      "cohorte": ["2017-01", "2017-03", "2017-05", "2017-07", "2017-09", "2017-11"],
      "taille_cohorte": [743, 2554, 3451, 3810, 4012, 7060],
      "pct_retour_m1": [0.27, 0.39, 0.17, 0.52, 0.35, 0.23],
      "pct_retour_m3": [0.13, 0.24, 0.29, 0.34, 0.20, 0.18],
      "pct_retour_m6": [0.27, 0.20, 0.17, 0.21, 0.15, 0.14],
  }
  df_coh = pd.DataFrame(data_cohortes)
  st.dataframe(df_coh)
  st.info(
      "💡 Constat de l'analyse : Moins de 1 % des clients repassent commande à"
      " 1, 3 ou 6 mois, montrant une marketplace vivant principalement"
      " d'acheteurs uniques."
  )

elif menu == "Statuts des Commandes":
  st.header("📦 Répartition des Statuts de Commandes")
  st.markdown("Basé sur le script `04_statuts_commandes.sql`.")

  data_statuts = {
      "order_status": [
          "delivered",
          "shipped",
          "canceled",
          "unavailable",
          "invoiced",
          "processing",
          "created",
      ],
      "pourcentage": [97.02, 1.15, 0.63, 0.31, 0.31, 0.30, 0.05],
  }
  df_stat = pd.DataFrame(data_statuts)

  fig_pie = px.pie(
      df_stat,
      names="order_status",
      values="pourcentage",
      title="Répartition globale des statuts de commandes",
  )
  st.plotly_chart(fig_pie, use_container_width=True)
  st.dataframe(df_stat)

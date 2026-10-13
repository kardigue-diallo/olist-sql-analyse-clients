import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Olist E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)

# Titre principal
st.title("📊 Tableau de bord - Olist E-Commerce Analytics")
st.markdown(
    "Application interactive mettant en valeur l'analyse SQL complète des **9"
    " tables** de la marketplace Olist."
)

# Menu latéral de navigation enrichi
menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Accueil & Contexte (9 tables)",
        "Chiffre d'Affaires & Croissance",
        "Segmentation RFM (Clients)",
        "Rétention par Cohortes",
        "Statuts & Logistique",
        "Avis & Satisfaction Client",
        "Vendeurs & Géolocalisation",
    ],
)

if menu == "Accueil & Contexte (9 tables)":
  st.header("Bienvenue sur le dashboard d'analyse Olist !")
  st.write(
      "Ce projet analyse une marketplace e-commerce brésilienne à travers"
      " des requêtes SQL pures (SQLite) exploitant l'ensemble des données"
      " relationnelles."
  )

  # Indicateurs clés (KPIs)
  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Commandes totales", "99 441", "+97% livrées")
  col2.metric("Clients uniques", "96 096", "Base unifiée")
  col3.metric("Chiffre d'Affaires", "13.2M R$", "Ventes validées")
  col4.metric("Tables exploitées", "9 / 9", "Intégralité du projet")

  st.markdown("### 📁 Les 9 tables analysées dans le dépôt :")
  st.markdown("""
    - `olist_orders_dataset` (Commandes)
    - `olist_customers_dataset` (Clients)
    - `olist_order_items_dataset` (Lignes de commande)
    - `olist_order_payments_dataset` (Paiements)
    - `olist_order_reviews_dataset` (Avis et notes)
    - `olist_products_dataset` (Produits)
    - `olist_sellers_dataset` (Vendeurs)
    - `olist_geolocation_dataset` (Géolocalisation)
    - `product_category_name_translation` (Traduction des catégories)
    """)

elif menu == "Chiffre d'Affaires & Croissance":
  st.header("📈 Évolution Dynamique du Chiffre d'Affaires")
  st.markdown(
      "Visualisation interactive avec curseur temporel pour analyser la"
      " croissance et la décroissance."
  )

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

  # Graphique Plotly avec curseur interactif (range slider)
  fig = px.area(
      df_ca,
      x="mois",
      y="chiffre_affaires",
      markers=True,
      title="Croissance Mensuelle du Chiffre d'Affaires",
      color_discrete_sequence=["#2b5c8f"],
  )

  fig.update_layout(
      xaxis=dict(
          rangeselector=dict(
              buttons=[
                  dict(count=3, label="3m", step="month", stepmode="backward"),
                  dict(count=6, label="6m", step="month", stepmode="backward"),
                  dict(step="all", label="Tout afficher"),
              ]
          ),
          rangeslider=dict(visible=True),
          type="category",
      )
  )

  st.plotly_chart(fig, use_container_width=True)

  st.subheader("Tableau détaillé")
  st.dataframe(df_ca)

elif menu == "Segmentation RFM (Clients)":
  st.header("🎯 Analyse RFM et Segmentation Client")
  st.markdown("Répartition des clients selon leur Récence, Fréquence et Montant.")

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
      text="ca_segment",
      title="Contribution au Chiffre d'Affaires par Segment",
      color="segment",
  )
  fig_bar.update_traces(texttemplate="%{text:.2s}", textposition="outside")
  st.plotly_chart(fig_bar, use_container_width=True)

  st.dataframe(df_seg)

elif menu == "Rétention par Cohortes":
  st.header("🔄 Analyse de Rétention par Cohortes Mensuelles")
  st.markdown("Mesure du taux de rachat des clients à M1, M3 et M6.")

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
      "💡 **Insight :** Moins de 1 % des clients repassent commande à M1, M3"
      " ou M6, confirmant que la marketplace repose principalement sur des"
      " acheteurs uniques."
  )

elif menu == "Statuts & Logistique":
  st.header("📦 État des Commandes et Logistique")
  st.markdown("Analyse des statuts de commandes issus de la table orders.")

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
      hole=0.4,
      title="Répartition Globale des Statuts de Commandes",
  )
  st.plotly_chart(fig_pie, use_container_width=True)
  st.dataframe(df_stat)

elif menu == "Avis & Satisfaction Client":
  st.header("⭐ Analyse des Avis Clients")
  st.markdown("Exploitation de la table des avis pour évaluer la satisfaction.")

  data_reviews = {
      "Note (Stars)": ["5 Étoiles", "4 Étoiles", "3 Étoiles", "2 Étoiles", "1 Étoile"],
      "Pourcentage": [57.3, 19.1, 8.3, 3.2, 12.1],
  }
  df_rev = pd.DataFrame(data_reviews)

  fig_rev = px.bar(
      df_rev,
      x="Note (Stars)",
      y="Pourcentage",
      color="Note (Stars)",
      title="Distribution des Notes Attribuées par les Clients",
  )
  st.plotly_chart(fig_rev, use_container_width=True)
  st.dataframe(df_rev)

elif menu == "Vendeurs & Géolocalisation":
  st.header("🌍 Performance des Vendeurs et Répartition Géographique")
  st.markdown(
      "Exploitation des tables de géolocalisation et des vendeurs partenaires."
  )

  col1, col2 = st.columns(2)
  with col1:
    st.subheader("Top Régions / États")
    df_geo = pd.DataFrame({
        "État": [
            "São Paulo (SP)",
            "Rio de Janeiro (RJ)",
            "Minas Gerais (MG)",
            "Rio Grande do Sul (RS)",
        ],
        "Part (%)": [42.1, 12.8, 11.6, 5.4],
    })
    st.dataframe(df_geo)

  with col2:
    st.subheader("Écosystème Vendeurs")
    st.metric("Nombre total de vendeurs actifs", "3 095", "Actifs sur la plateforme")
    st.info(
        "💡 Les requêtes multi-tables permettent de lier chaque article vendu"
        " à son vendeur d'origine."
    )

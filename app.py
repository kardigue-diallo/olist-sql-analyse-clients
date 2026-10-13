import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Configuration de la page Streamlit
st.set_page_config(
    page_title="Olist E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)


# 2. Style CSS épuré et moderne
def apply_clean_theme():
  st.markdown(
      """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        }
        .block-container {
            background-color: #ffffff;
            padding: 2rem 3rem;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
            margin-top: 1rem;
        }
        h1, h2, h3 {
            color: #0f172a;
            font-weight: 700;
        }
        /* Style des images d'illustration sous les titres */
        .stImage img {
            border-radius: 12px;
            max-height: 200px;
            object-fit: cover;
            margin-top: 10px;
            margin-bottom: 20px;
        }
        </style>
        """,
      unsafe_allow_html=True,
  )


apply_clean_theme()

# 3. Menu latéral
st.sidebar.title("📌 Navigation SQL")
menu = st.sidebar.selectbox(
    "Choisir une analyse :",
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

# --- PAGE 1 : ACCUEIL ---
if menu == "Accueil & Contexte (9 tables)":
  st.title("📊 Tableau de bord - Olist E-Commerce Analytics")
  st.markdown(
      "Application interactive complète mettant en valeur l'analyse SQL des **9"
      " tables** de la marketplace Olist."
  )
  st.image(
      "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1000&auto=format&fit=crop",
      use_container_width=True,
  )

  st.divider()

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Commandes totales", "99 441", "+97% livrées")
  col2.metric("Clients uniques", "96 096", "Base unifiée")
  col3.metric("Chiffre d'Affaires", "13.2M R$", "Ventes validées")
  col4.metric("Tables exploitées", "9 / 9", "Projet complet")

  st.divider()

  st.markdown("### 📁 Les 9 tables analysées dans le modèle :")
  col_a, col_b = st.columns(2)
  with col_a:
    st.markdown("""
        * `olist_orders_dataset` (Commandes)
        * `olist_customers_dataset` (Clients)
        * `olist_order_items_dataset` (Articles)
        * `olist_order_payments_dataset` (Paiements)
        * `olist_order_reviews_dataset` (Avis)
        """)
  with col_b:
    st.markdown("""
        * `olist_products_dataset` (Catalogue produits)
        * `olist_sellers_dataset` (Vendeurs)
        * `olist_geolocation_dataset` (Coordonnées geo)
        * `product_category_name_translation` (Traductions)
        """)

# --- PAGE 2 : CHIFFRE D'AFFAIRES ---
elif menu == "Chiffre d'Affaires & Croissance":
  st.title("📈 Évolution et Analyse Dynamique du Chiffre d'Affaires")
  st.markdown(
      "Pilotez l'évolution temporelle pour analyser chaque variation réelle de"
      " votre requête SQL."
  )
  st.image(
      "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?q=80&w=1000&auto=format&fit=crop",
      use_container_width=True,
  )

  data_ca = [
      {
          "mois": "2017-01",
          "ca": 111798.0,
          "tendance": "Lancement stable",
          "explication": (
              "Démarrage de l'activité sur la marketplace Olist avec un"
              " premier socle de commandes."
          ),
      },
      {
          "mois": "2017-02",
          "ca": 234000.0,
          "tendance": "Forte hausse (+109%)",
          "explication": (
              "Première belle accélération grâce à l'acquisition de nouveaux"
              " clients et vendeurs."
          ),
      },
      {
          "mois": "2017-03",
          "ca": 359000.0,
          "tendance": "Hausse continue (+53%)",
          "explication": (
              "Confirmation de la croissance trimestrielle et du volume"
              " d'articles."
          ),
      },
      {
          "mois": "2017-04",
          "ca": 410000.0,
          "tendance": "Progression régulière (+14%)",
          "explication": (
              "Stabilisation de la dynamique de commande, panier moyen"
              " maintenu."
          ),
      },
      {
          "mois": "2017-05",
          "ca": 590000.0,
          "tendance": "Pic de croissance (+44%)",
          "explication": (
              "Gros pic d'activité stimulé par des campagnes et l'élargissement"
              " du catalogue."
          ),
      },
      {
          "mois": "2017-06",
          "ca": 510000.0,
          "tendance": "Légère baisse (-13%)",
          "explication": (
              "Correction naturelle après le record de mai, réajustement des"
              " volumes."
          ),
      },
      {
          "mois": "2017-07",
          "ca": 481605.0,
          "tendance": "Stabilisation",
          "explication": (
              "Phase de palier estivale, la demande globale reste stable."
          ),
      },
      {
          "mois": "2017-08",
          "ca": 670000.0,
          "tendance": "Forte reprise (+39%)",
          "explication": (
              "Nouvelle impulsion forte portée par l'arrivée de vendeurs"
              " actifs."
          ),
      },
      {
          "mois": "2017-09",
          "ca": 720000.0,
          "tendance": "Hausse soutenue (+7%)",
          "explication": (
              "La rentrée s'accompagne d'un trafic accru et de transactions"
              " en hausse."
          ),
      },
      {
          "mois": "2017-10",
          "ca": 770000.0,
          "tendance": "Croissance continue (+7%)",
          "explication": (
              "Préparation progressive des périodes de fin d'année."
          ),
      },
      {
          "mois": "2017-11",
          "ca": 1180000.0,
          "tendance": "Record historique (+53%)",
          "explication": (
              "🚀 **Black Friday !** Pic absolu de chiffre d'affaires de toute"
              " la période."
          ),
      },
      {
          "mois": "2017-12",
          "ca": 950000.0,
          "tendance": "Fin d'année élevée",
          "explication": (
              "Volumes de fêtes très élevés, confirmant la forte saisonnalité."
          ),
      },
  ]
  df_ca = pd.DataFrame(data_ca)

  col_g, col_d = st.columns([2, 1])
  with col_g:
    mois_sel = st.select_slider(
        "Faites glisser pour faire évoluer la courbe :",
        options=df_ca["mois"].tolist(),
    )
    df_f = df_ca[df_ca["mois"] <= mois_sel]
    fig = px.area(
        df_f,
        x="mois",
        y="ca",
        markers=True,
        range_x=["2017-01", "2017-12"],
        range_y=[0, 1350000],
        title="Évolution du Chiffre d'Affaires (en R$)",
    )
    fig.update_traces(line_color="#2563eb", fillcolor="rgba(37, 99, 235, 0.2)")
    st.plotly_chart(fig, use_container_width=True)

  with col_d:
    st.markdown("### 💡 Analyse du mois")
    info = df_ca[df_ca["mois"] == mois_sel].iloc[0]
    st.info(f"**Mois :** {info['mois']}")
    st.metric("Chiffre d'Affaires", f"{info['ca']:,.0f} R$")
    st.markdown(f"**Tendance :** `{info['tendance']}`")
    st.markdown(f"**Explication :**\n{info['explication']}")

# --- PAGE 3 : SEGMENTATION RFM ---
elif menu == "Segmentation RFM (Clients)":
  st.title("🎯 Segmentation RFM des Clients")
  st.markdown("Analyse croisée Récence, Fréquence et Montant.")
  st.image(
      "

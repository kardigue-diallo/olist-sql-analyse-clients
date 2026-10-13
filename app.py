import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Configuration de la page Streamlit
st.set_page_config(
    page_title="Olist E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)


# 2. Style CSS épuré et moderne (fond doux, pas de fausses photos)
def apply_clean_theme():
  st.markdown(
      """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        }
        .block-container {
            background-color: #ffffff;
            padding: 2.5rem 3rem;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
            margin-top: 1rem;
        }
        h1, h2, h3 {
            color: #0f172a;
            font-weight: 700;
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
      "Application interactive mettant en valeur l'analyse SQL globale des"
      " **9 tables** de la marketplace Olist."
  )

  st.divider()

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Commandes totales", "99 441", "+97% livrées")
  col2.metric("Clients uniques", "96 096", "Base unifiée")
  col3.metric("Chiffre d'Affaires", "13.2M R$", "Ventes validées")
  col4.metric("Tables exploitées", "9 / 9", "Projet complet")

  st.divider()

  st.markdown("### 📁 Structure relationnelle des 9 tables analysées :")
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
        * `olist_geolocation_dataset` (Coordonnées géo)
        * `product_category_name_translation` (Traductions)
        """)

# --- PAGE 2 : CHIFFRE D'AFFAIRES ---
elif menu == "Chiffre d'Affaires & Croissance":
  st.title("📈 Évolution et Analyse Dynamique du Chiffre d'Affaires")
  st.markdown(
      "Pilotez le curseur pour observer la croissance et lire l'explication"
      " contextuelle de chaque mois."
  )

  data_ca = [
      {
          "mois": "2017-01",
          "ca": 111798.0,
          "tendance": "Lancement stable",
          "explication": (
              "Démarrage de l'activité sur Olist avec un premier socle de"
              " commandes."
          ),
      },
      {
          "mois": "2017-02",
          "ca": 234000.0,
          "tendance": "Forte hausse (+109%)",
          "explication": (
              "Accélération liée à l'acquisition de nouveaux clients et"
              " vendeurs."
          ),
      },
      {
          "mois": "2017-03",
          "ca": 359000.0,
          "tendance": "Hausse continue (+53%)",
          "explication": (
              "Confirmation de la croissance trimestrielle et hausse des"
              " volumes."
          ),
      },
      {
          "mois": "2017-04",
          "ca": 410000.0,
          "tendance": "Progression régulière (+14%)",
          "explication": (
              "Stabilisation des commandes, panier moyen bien maintenu."
          ),
      },
      {
          "mois": "2017-05",
          "ca": 590000.0,
          "tendance": "Pic de croissance (+44%)",
          "explication": (
              "Pic d'activité stimulé par l'élargissement du catalogue."
          ),
      },
      {
          "mois": "2017-06",
          "ca": 510000.0,
          "tendance": "Légère baisse (-13%)",
          "explication": (
              "Correction naturelle des volumes après le mois record de mai."
          ),
      },
      {
          "mois": "2017-07",
          "ca": 481605.0,
          "tendance": "Stabilisation",
          "explication": (
              "Palier estival : demande globale stable sur les catégories"
              " phares."
          ),
      },
      {
          "mois": "2017-08",
          "ca": 670000.0,
          "tendance": "Forte reprise (+39%)",
          "explication": (
              "Nouvelle dynamique tirée par l'arrivée de vendeurs actifs."
          ),
      },
      {
          "mois": "2017-09",
          "ca": 720000.0,
          "tendance": "Hausse soutenue (+7%)",
          "explication": (
              "Augmentation du volume de transactions lors de la rentrée."
          ),
      },
      {
          "mois": "2017-10",
          "ca": 770000.0,
          "tendance": "Croissance continue (+7%)",
          "explication": (
              "Préparation progressive des grands événements de fin d'année."
          ),
      },
      {
          "mois": "2017-11",
          "ca": 1180000.0,
          "tendance": "Record historique (+53%)",
          "explication": (
              "🚀 Black Friday ! Sommet absolu des ventes sur la période."
          ),
      },
      {
          "mois": "2017-12",
          "ca": 950000.0,
          "tendance": "Fin d'année élevée",
          "explication": (
              "Fort volume lié aux fêtes, confirmant la saisonnalité."
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
        title="Évolution du Chiffre d'Affaires (R$)",
    )
    fig.update_traces(line_color="#2563eb", fillcolor="rgba(37, 99, 235, 0.2)")
    st.plotly_chart(fig, use_container_width=True)

  with col_d:
    st.markdown("### 💡 Fenêtre d'analyse")
    info = df_ca[df_ca["mois"] == mois_sel].iloc[0]
    st.info(f"**Mois :** {info['mois']}")
    st.metric("Chiffre d'Affaires", f"{info['ca']:,.0f} R$")
    st.markdown(f"**Tendance :** `{info['tendance']}`")
    st.markdown(f"**Explication :**\n{info['explication']}")

# --- PAGE 3 : SEGMENTATION RFM ---
elif menu == "Segmentation RFM (Clients)":
  st.title("🎯 Segmentation RFM des Clients")
  st.markdown("Analyse croisée de la Récence, la Fréquence et du Montant.")

  data_rfm = [
      {
          "segment": "Gros acheteurs récents",
          "clients": 14519,
          "ca": 3877678.0,
          "desc": (
              "Cœur de valeur : clients fidèles avec des achats fréquents et"
              " récents."
          ),
      },
      {
          "segment": "À risque (gros montant)",
          "clients": 13746,
          "ca": 3806579.0,
          "desc": (
              "Gros paniers historiques mais inactifs récemment. Cible de"
              " relance."
          ),
      },
      {
          "segment": "Occasionnels",
          "clients": 18067,
          "ca": 2348240.0,
          "desc": "Achats modérés, représente une base très large.",
      },
      {
          "segment": "Perdus",
          "clients": 22610,
          "ca": 1259040.0,
          "desc": "Anciens clients sans nouvelle commande depuis longtemps.",
      },
      {
          "segment": "Nouveaux clients",
          "clients": 21615,
          "ca": 1201552.0,
          "desc": "Premier achat récent, potentiel de fidélisation.",
      },
      {
          "segment": "Fidèles actifs",
          "clients": 1813,
          "ca": 484852.0,
          "desc": "Fréquence de rachat élevée et régulière.",
      },
      {
          "segment": "Fidèles endormis",
          "clients": 988,
          "ca": 243556.0,
          "desc": "Anciens clients très réguliers en perte d'activité.",
      },
  ]
  df_rfm = pd.DataFrame(data_rfm)

  col_g, col_d = st.columns([2, 1])
  with col_g:
    fig_bar = px.bar(
        df_rfm,
        x="segment",
        y="ca",
        color="segment",
        title="Contribution au CA par Segment (R$)",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

  with col_d:
    st.markdown("### 🔍 Audit de segment")
    seg_choisi = st.selectbox(
        "Choisir un segment :", df_rfm["segment"].tolist()
    )
    det = df_rfm[df_rfm["segment"] == seg_choisi].iloc[0]
    st.info(f"**Segment :** {det['segment']}")
    st.metric("Nombre de clients", f"{det['clients']:,}")
    st.metric("Chiffre d'Affaires", f"{det['ca']:,.0f} R$")
    st.markdown(f"**Diagnostic :**\n{det['desc']}")

# --- PAGE 4 : COHORTES ---
elif menu == "Rétention par Cohortes":
  st.title("🔄 Analyse de Rétention par Cohortes")
  st.markdown("Suivi du taux de rachat à M1, M3 et M6.")

  data_coh = [
      {
          "cohorte": "2017-01",
          "taille": 743,
          "m1": 0.27,
          "m3": 0.13,
          "m6": 0.27,
          "analyse": "Cohorte initiale avec comportements restreints.",
      },
      {
          "cohorte": "2017-03",
          "taille": 2554,
          "m1": 0.39,
          "m3": 0.24,
          "m6": 0.20,
          "analyse": "Bon retour initial à M1 (0.39%).",
      },
      {
          "cohorte": "2017-05",
          "taille": 3451,
          "m1": 0.17,
          "m3": 0.29,
          "m6": 0.17,
          "analyse": "Leger pic de réachat observé à 3 mois.",
      },
      {
          "cohorte": "2017-07",
          "taille": 3810,
          "m1": 0.52,
          "m3": 0.34,
          "m6": 0.21,
          "analyse": "Excellente performance de rétention estivale.",
      },
      {
          "cohorte": "2017-09",
          "taille": 4012,
          "m1": 0.35,
          "m3": 0.20,
          "m6": 0.15,
          "analyse": "Rétention de rentrée stable.",
      },
      {
          "cohorte": "2017-11",
          "taille": 7060,
          "m1": 0.23,
          "m3": 0.18,
          "m6": 0.14,
          "analyse": "Volume poussé par le Black Friday mais faible rachat.",
      },
  ]
  df_c = pd.DataFrame(data_coh)

  col_g, col_d = st.columns([2, 1])
  with col_g:
    coh_sel = st.selectbox(
        "Sélectionner une cohorte :", df_c["cohorte"].tolist()
    )
    df_f_c = df_c[df_c["cohorte"] == coh_sel]
    st.dataframe(
        df_f_c[["cohorte", "taille", "m1", "m3", "m6"]], use_container_width=True
    )
    st.warning(
        "💡 **Conclusion SQL :** Taux de rachat global < 1%, confirmant des"
        " achats uniques."
    )

  with col_d:
    st.markdown("### 📋 Explication Cohorte")
    info_c = df_f_c.iloc[0]
    st.markdown(f"**Cohorte :** {info_c['cohorte']}")
    st.metric("Taille initiale", f"{info_c['taille']:,} clients")
    st.markdown(f"**Diagnostic :**\n{info_c['analyse']}")

# --- PAGE 5 : LOGISTIQUE ---
elif menu == "Statuts & Logistique":
  st.title("📦 Analyse Logistique & Statuts")
  st.markdown("Ventilation des états de traitement des commandes.")

  data_st = [
      {
          "statut": "delivered",
          "pct": 97.02,
          "desc": "Commandes livrées avec succès.",
      },
      {"statut": "shipped", "pct": 1.15, "desc": "En cours d'acheminement."},
      {"statut": "canceled", "pct": 0.63, "desc": "Annulées avant livraison."},
      {
          "statut": "unavailable",
          "pct": 0.31,
          "desc": "Stock indisponible chez le vendeur.",
      },
      {"statut": "invoiced", "pct": 0.31, "desc": "Facturées, en attente d'envoi."},
      {"statut": "processing", "pct": 0.30, "desc": "En cours de préparation."},
      {"statut": "created", "pct": 0.05, "desc": "Créées, paiement non validé."},
  ]
  df_st = pd.DataFrame(data_st)

  col_g, col_d = st.columns([2, 1])
  with col_g:
    fig_pie = px.pie(
        df_st,
        names="statut",
        values="pct",
        hole=0.4,
        title="Répartition des Statuts de Commandes (%)",
    )
    st.plotly_chart(fig_pie, use_container_width=True)

  with col_d:
    st.markdown("### 🔍 Performance Logistique")
    st.success("Taux de livraison validé : **97.02%**")
    st.write(
        "Le taux de commandes annulées ou indisponibles reste maîtrisé sous 1%."
    )

# --- PAGE 6 : AVIS CLIENTS ---
elif menu == "Avis & Satisfaction Client":
  st.title("⭐ Analyse de la Satisfaction Client")
  st.markdown("Répartition des notes laissées par les clients.")

  data_rev = [
      {"note": "5 Étoiles", "pct": 57.3, "avis": "Excellente satisfaction."},
      {"note": "4 Étoiles", "pct": 19.1, "avis": "Très bonne évaluation."},
      {"note": "3 Étoiles", "pct": 8.3, "avis": "Avis mitigé."},
      {"note": "2 Étoiles", "pct": 3.2, "avis": "Insatisfaction partielle."},
      {"note": "1 Étoile", "pct": 12.1, "avis": "Insatisfaction majeure."},
  ]
  df_r = pd.DataFrame(data_rev)

  col_g, col_d = st.columns([2, 1])
  with col_g:
    fig_rev = px.bar(
        df_r,
        x="note",
        y="pct",
        color="note",
        title="Distribution des Notes Clients (%)",
    )
    st.plotly_chart(fig_rev, use_container_width=True)

  with col_d:
    st.markdown("### 💡 Synthèse Satisfaction")
    note_sel = st.selectbox("Choisir une note :", df_r["note"].tolist())
    r_info = df_r[df_r["note"] == note_sel].iloc[0]
    st.metric("Part des avis", f"{r_info['pct']}%")
    st.markdown(f"**Détail :**\n{r_info['avis']}")

# --- PAGE 7 : GEOLOCALISATION ---
elif menu == "Vendeurs & Géolocalisation":
  st.title("🌍 Géolocalisation & Vendeurs Partenaires")
  st.markdown("Répartition géographique des ventes.")

  col1, col2 = st.columns(2)
  with col1:
    st.subheader("Top États (Volume de Ventes)")
    df_geo = pd.DataFrame({
        "État": [
            "São Paulo (SP)",
            "Rio de Janeiro (RJ)",
            "Minas Gerais (MG)",
            "Rio Grande do Sul (RS)",
        ],
        "Part (%)": [42.1, 12.8, 11.6, 5.4],
    })
    st.dataframe(df_geo, use_container_width=True)

  with col2:
    st.subheader("Réseau Vendeurs")
    st.metric("Vendeurs enregistrés", "3 095", "Actifs dans l'écosystème")
    st.info(
        "💡 L'État de São Paulo (SP) concentre la majorité de l'activité"
        " commerciale et logistique."
    )

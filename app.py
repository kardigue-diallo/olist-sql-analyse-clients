import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Configuration de la page Streamlit
st.set_page_config(
    page_title="Olist E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
)


# 2. Fonction de style : Fond d'écran brouillard (flouté) et conteneur translucide
def apply_custom_style():
  st.markdown(
      """
        <style>
        /* Fond d'écran global avec superposition douce */
        .stApp {
            background: linear-gradient(rgba(245, 247, 250, 0.85), rgba(245, 247, 250, 0.85)), 
                        url("https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1920&auto=format&fit=crop");
            background-size: cover;
            background-attachment: fixed;
        }
        
        /* Effet brouillard / verre dépoli sur le bloc principal */
        .block-container {
            background-color: rgba(255, 255, 255, 0.88);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 2.5rem;
            border-radius: 18px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }

        /* Arrondir les images de bannière */
        .stImage > img {
            border-radius: 12px;
            max-height: 220px;
            object-fit: cover;
            margin-bottom: 1rem;
        }
        </style>
        """,
      unsafe_allow_html=True,
  )


apply_custom_style()

# 3. Menu latéral de navigation
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

# --- PAGE 1 : ACCUEIL ---
if menu == "Accueil & Contexte (9 tables)":
  st.image(
      "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop",
      use_container_width=True,
  )
  st.title("📊 Tableau de bord - Olist E-Commerce Analytics")
  st.markdown(
      "Application interactive complète mettant en valeur l'analyse SQL des **9"
      " tables** de la marketplace Olist."
  )

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Commandes totales", "99 441", "+97% livrées")
  col2.metric("Clients uniques", "96 096", "Base unifiée")
  col3.metric("Chiffre d'Affaires", "13.2M R$", "Ventes validées")
  col4.metric("Tables exploitées", "9 / 9", "Intégralité du projet")

  st.markdown("### 📁 Les 9 tables du projet :")
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

# --- PAGE 2 : CHIFFRE D'AFFAIRES ---
elif menu == "Chiffre d'Affaires & Croissance":
  st.image(
      "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop",
      use_container_width=True,
  )
  st.header("📈 Évolution et Analyse Dynamique du Chiffre d'Affaires")
  st.markdown("Pilotez l'évolution temporelle pour analyser chaque variation.")

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
        "Sélectionnez le mois à analyser :", options=df_ca["mois"].tolist()
    )
    df_f = df_ca[df_ca["mois"] <= mois_sel]
    fig = px.area(
        df_f,
        x="mois",
        y="ca",
        markers=True,
        range_x=["2017-01", "2017-12"],
        range_y=[0, 1350000],
        title="Évolution du Chiffre d'Affaires",
    )
    st.plotly_chart(fig, use_container_width=True)

  with col_d:
    st.markdown("### 💡 Analyse en direct")
    info = df_ca[df_ca["mois"] == mois_sel].iloc[0]
    st.info(f"**Mois :** {info['mois']}")
    st.metric("Chiffre d'Affaires", f"{info['ca']:,.0f} R$")
    st.markdown(f"**Tendance :** `{info['tendance']}`")
    st.markdown(f"**Explication :**\n{info['explication']}")

# --- PAGE 3 : SEGMENTATION RFM ---
elif menu == "Segmentation RFM (Clients)":
  st.image(
      "https://images.unsplash.com/photo-1556742049-0a670f4a458d?q=80&w=1200&auto=format&fit=crop",
      use_container_width=True,
  )
  st.header("🎯 Exploration Interactive des Segments RFM")
  st.markdown(
      "Cliquez sur un segment pour comprendre sa valeur pour la marketplace."
  )

  data_rfm = [
      {
          "segment": "Gros acheteurs récents",
          "clients": 14519,
          "ca": 3877678.0,
          "desc": (
              "Le cœur de valeur de la marketplace : achètent souvent, ont"
              " acheté récemment et dépensent beaucoup."
          ),
      },
      {
          "segment": "À risque (gros montant)",
          "clients": 13746,
          "ca": 3806579.0,
          "desc": (
              "Gros paniers historiques mais dont la date de dernière commande"
              " commence à dater. Nécessitent des campagnes de réactivation."
          ),
      },
      {
          "segment": "Occasionnels",
          "clients": 18067,
          "ca": 2348240.0,
          "desc": (
              "Clients réguliers ou modérés représentant un volume de base stable"
              " mais nécessitant du upsell."
          ),
      },
      {
          "segment": "Perdus",
          "clients": 22610,
          "ca": 1259040.0,
          "desc": (
              "Anciens clients inactifs depuis longtemps et générant de"
              " faibles montants actuels."
          ),
      },
      {
          "segment": "Nouveaux clients",
          "clients": 21615,
          "ca": 1201552.0,
          "desc": (
              "Acquisition récente, fort potentiel de transformation en clients"
              " fidèles."
          ),
      },
      {
          "segment": "Fidèles actifs",
          "clients": 1813,
          "ca": 484852.0,
          "desc": (
              "Fréquence de rachat élevée, ambassadeurs naturels de la"
              " plateforme."
          ),
      },
      {
          "segment": "Fidèles endormis",
          "clients": 988,
          "ca": 243556.0,
          "desc": (
              "Anciens clients très fidèles qu'il faut relancer en priorité"
              " pour éviter l'attrition définitive."
          ),
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
        title="Chiffre d'Affaires par Segment RFM",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

  with col_d:
    st.markdown("### 🔍 Détail du segment")
    seg_choisi = st.selectbox(
        "Choisissez un segment à auditer :", df_rfm["segment"].tolist()
    )
    det = df_rfm[df_rfm["segment"] == seg_choisi].iloc[0]
    st.info(f"**Segment :** {det['segment']}")
    st.metric("Clients concernés", f"{det['clients']:,}")
    st.metric("CA du segment", f"{det['ca']:,.0f} R$")
    st.markdown(f"**Stratégie / Analyse :**\n{det['desc']}")

# --- PAGE 4 : COHORTES ---
elif menu == "Rétention par Cohortes":
  st.image(
      "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?q=80&w=1200&auto=format&fit=crop",
      use_container_width=True,
  )
  st.header("🔄 Analyse Dynamique de Rétention par Cohortes")
  st.markdown(
      "Évolution du taux de retour client à M1, M3 et M6 selon la cohorte"
      " d'origine."
  )

  data_coh = [
      {
          "cohorte": "2017-01",
          "taille": 743,
          "m1": 0.27,
          "m3": 0.13,
          "m6": 0.27,
          "analyse": "Cohorte initiale restreinte, comportement de réachat volatil.",
      },
      {
          "cohorte": "2017-03",
          "taille": 2554,
          "m1": 0.39,
          "m3": 0.24,
          "m6": 0.20,
          "analyse": "Bon taux de retour à M1 (0.39%) avant une stabilisation.",
      },
      {
          "cohorte": "2017-05",
          "taille": 3451,
          "m1": 0.17,
          "m3": 0.29,
          "m6": 0.17,
          "analyse": "Pic de rétention à M3 (0.29%), témoignant d'une fidélité à moyen terme.",
      },
      {
          "cohorte": "2017-07",
          "taille": 3810,
          "m1": 0.52,
          "m3": 0.34,
          "m6": 0.21,
          "analyse": "Meilleure cohorte globale en termes de retour à M1 (0.52%).",
      },
      {
          "cohorte": "2017-09",
          "taille": 4012,
          "m1": 0.35,
          "m3": 0.20,
          "m6": 0.15,
          "analyse": "Rétention correcte à l'approche de la fin d'année.",
      },
      {
          "cohorte": "2017-11",
          "taille": 7060,
          "m1": 0.23,
          "m3": 0.18,
          "m6": 0.14,
          "analyse": (
              "Gros volume de la cohorte Black Friday, mais dilution du taux"
              " de rachat global."
          ),
      },
  ]
  df_c = pd.DataFrame(data_coh)

  col_g, col_d = st.columns([2, 1])
  with col_g:
    coh_sel = st.selectbox(
        "Sélectionnez une cohorte mensuelle :", df_c["cohorte"].tolist()
    )
    df_f_c = df_c[df_c["cohorte"] == coh_sel]
    st.dataframe(
        df_f_c[["cohorte", "taille", "m1", "m3", "m6"]], use_container_width=True
    )
    st.info(
        "💡 **Constat général :** Moins de 1 % des clients repassent commande,"
        " traduisant un modèle à acheteurs uniques."
    )

  with col_d:
    st.markdown("### 📋 Explication de la cohorte")
    info_c = df_f_c.iloc[0]
    st.markdown(f"**Mois d'origine :** {info_c['cohorte']}")
    st.metric("Taille de la cohorte", f"{info_c['taille']:,} clients")
    st.markdown(f"**Diagnostic :**\n{info_c['analyse']}")

# --- PAGE 5 : LOGISTIQUE ---
elif menu == "Statuts & Logistique":
  st.image(
      "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1200&auto=format&fit=crop",
      use_container_width=True,
  )
  st.header("📦 Analyse des Statuts de Commandes & Logistique")
  st.markdown("Découvrez la performance logistique et le taux de livraison.")

  data_st = [
      {
          "statut": "delivered",
          "pct": 97.02,
          "desc": (
              "Commandes livrées avec succès. C'est le cœur de l'activité"
              " logistique."
          ),
      },
      {
          "statut": "shipped",
          "pct": 1.15,
          "desc": "Commandes expédiées et actuellement en cours d'acheminement.",
      },
      {
          "statut": "canceled",
          "pct": 0.63,
          "desc": (
              "Commandes annulées (par le client ou suite à une rupture de"
              " stock)."
          ),
      },
      {
          "statut": "unavailable",
          "pct": 0.31,
          "desc": "Articles indisponibles au moment du traitement.",
      },
      {
          "statut": "invoiced",
          "pct": 0.31,
          "desc": "Commandes facturées mais en attente d'expédition.",
      },
      {
          "statut": "processing",
          "pct": 0.30,
          "desc": "Commandes en cours de préparation logistique.",
      },
      {
          "statut": "created",
          "pct": 0.05,
          "desc": "Commandes créées mais non encore payées ou traitées.",
      },
  ]
  df_st = pd.DataFrame(data_st)

  col_g, col_d = st.columns([2, 1])
  with col_g:
    fig_pie = px.pie(
        df_st,
        names="statut",
        values="pct",
        hole=0.4,
        title="Répartition des Statuts de Commandes",
    )
    st.plotly_chart(fig_pie, use_container_width=True)

  with col_d:
    st.markdown("### 🔍 Focus Logistique")
    st.success("Taux de livraison global remarquable : **97.02%**")
    st.write(
        "Utilisez le graphique circulaire pour visualiser le poids infime des"
        " incidents par rapport aux commandes livrées."
    )

# --- PAGE 6 : AVIS CLIENTS ---
elif menu == "Avis & Satisfaction Client":
  st.image(
      "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop",
      use_container_width=True,
  )
  st.header("⭐ Analyse de la Satisfaction (Avis Clients)")
  st.markdown(
      "Évaluation de la qualité perçue à travers les notes de 1 à 5 étoiles."
  )

  data_rev = [
      {
          "note": "5 Étoiles",
          "pct": 57.3,
          "avis": "Expérience parfaite, livraison rapide et conforme.",
      },
      {
          "note": "4 Étoiles",
          "pct": 19.1,
          "avis": "Très satisfaisant, quelques détails mineurs.",
      },
      {
          "note": "3 Étoiles",
          "pct": 8.3,
          "avis": "Neutre : produit correct mais délais un peu longs.",
      },
      {
          "note": "2 Étoiles",
          "pct": 3.2,
          "avis": "Insatisfaction partielle (produit endommagé ou retard).",
      },
      {
          "note": "1 Étoile",
          "pct": 12.1,
          "avis": "Problème majeur (non livraison ou non-conformité grave).",
      },
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
    st.markdown("### 💡 Lecture des Avis")
    note_sel = st.selectbox("Sélectionner une note :", df_r["note"].tolist())
    r_info = df_r[df_r["note"] == note_sel].iloc[0]
    st.metric("Part des avis", f"{r_info['pct']}%")
    st.markdown(f"**Profil de l'avis :**\n{r_info['avis']}")

# --- PAGE 7 : GEOLOCALISATION ---
elif menu == "Vendeurs & Géolocalisation":
  st.image(
      "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?q=80&w=1200&auto=format&fit=crop",
      use_container_width=True,
  )
  st.header("🌍 Performance des Vendeurs & Géolocalisation")
  st.markdown("Analyse de la répartition territoriale de la marketplace.")

  col1, col2 = st.columns(2)
  with col1:
    st.subheader("Top États (Clients/Vendeurs)")
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
    st.subheader("Écosystème Partenaire")
    st.metric("Vendeurs actifs", "3 095", "Répartis sur le territoire")
    st.info(
        "💡 La concentration majeure dans l'État de São Paulo explique en"
        " grande partie l'efficacité des délais de livraison."
    )

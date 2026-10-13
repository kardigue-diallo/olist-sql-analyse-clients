import sqlite3
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


# Fonction de connexion à la base SQLite
@st.cache_data
def load_data(query):
  # Assurez-vous d'avoir mis votre fichier olist.db ou adaptez la source
  conn = sqlite3.connect("olist.db")
  df = pd.read_sql_query(query, conn)
  conn.close()
  return df


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
      " des requêtes SQL pures (SQLite)."
  )
  st.markdown(
      "Utilisez le menu de gauche pour basculer entre les différentes"
      " analyses."
  )

elif menu == "Chiffre d'Affaires Mensuel":
  st.header("📈 Évolution du Chiffre d'Affaires Mensuel")
  try:
    # Requête basée sur votre fichier 03_ca_mensuel.sql
    query_ca = """
        SELECT strftime('%Y-%m', o.order_purchase_timestamp) AS mois,
               COUNT(DISTINCT o.order_id) AS nb_commandes,
               ROUND(SUM(i.price), 2) AS chiffre_affaires,
               ROUND(SUM(i.price) / COUNT(DISTINCT o.order_id), 2) AS panier_moyen
        FROM olist_orders_dataset o
        JOIN olist_order_items_dataset i ON o.order_id = i.order_id
        WHERE o.order_status = 'delivered'
        GROUP BY mois
        ORDER BY mois;
        """
    df_ca = load_data(query_ca)

    if not df_ca.empty:
      fig = px.line(
          df_ca,
          x="mois",
          y="chiffre_affaires",
          markers=True,
          title="Chiffre d'Affaires Mensuel (en Réals)",
      )
      st.plotly_chart(fig, use_container_width=True)

      st.subheader("Détails mensuels")
      st.dataframe(df_ca)
    else:
      st.warning(
          "Base de données 'olist.db' introuvable ou vide sur le serveur."
      )
  except Exception as e:
    st.error(
        f"Erreur (Vérifiez la présence de 'olist.db' et des tables) : {e}"
    )

elif menu == "Segmentation RFM (Segments)":
  st.header("🎯 Répartition des Segments RFM")
  try:
    # Requête inspirée de votre fichier 07_rfm_segments.sql
    query_segments = """
        WITH base AS (
            SELECT c.customer_unique_id,
                   o.order_id,
                   o.order_purchase_timestamp,
                   SUM(i.price) AS montant_commande
            FROM olist_orders_dataset o
            JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
            JOIN olist_order_items_dataset i ON o.order_id = i.order_id
            WHERE o.order_status = 'delivered'
            GROUP BY c.customer_unique_id, o.order_id, o.order_purchase_timestamp
        ),
        ref AS (
            SELECT MAX(order_purchase_timestamp) AS date_ref FROM base
        ),
        rfm AS (
            SELECT b.customer_unique_id,
                   CAST(julianday((SELECT date_ref FROM ref)) - julianday(MAX(b.order_purchase_timestamp)) AS INTEGER) AS recence_jours,
                   COUNT(DISTINCT b.order_id) AS frequence,
                   SUM(b.montant_commande) AS montant_total
            FROM base b
            GROUP BY b.customer_unique_id
        ),
        scores AS (
            SELECT *,
                   NTILE(5) OVER (ORDER BY recence_jours DESC) AS r_score,
                   NTILE(5) OVER (ORDER BY montant_total ASC) AS m_score
            FROM rfm
        ),
        segments AS (
            SELECT *,
                   CASE
                       WHEN frequence >= 2 AND r_score >= 3 THEN 'Fidèles actifs'
                       WHEN frequence >= 2 THEN 'Fidèles endormis'
                       WHEN r_score >= 4 AND m_score >= 4 THEN 'Gros acheteurs récents'
                       WHEN r_score >= 4 THEN 'Nouveaux clients'
                       WHEN r_score <= 2 AND m_score >= 4 THEN 'À risque (gros montant)'
                       WHEN r_score <= 2 THEN 'Perdus'
                       ELSE 'Occasionnels'
                   END AS segment
            FROM scores
        )
        SELECT segment,
               COUNT(*) AS nb_clients,
               ROUND(SUM(montant_total), 2) AS ca_segment
        FROM segments
        GROUP BY segment
        ORDER BY ca_segment DESC;
        """
    df_seg = load_data(query_segments)
    if not df_seg.empty:
      fig_bar = px.bar(
          df_seg,
          x="segment",
          y="ca_segment",
          title="Chiffre d'Affaires par Segment RFM",
          color="segment",
      )
      st.plotly_chart(fig_bar, use_container_width=True)
      st.dataframe(df_seg)
    else:
      st.warning("Données indisponibles.")
  except Exception as e:
    st.error(f"Erreur lors du calcul RFM : {e}")

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
    "Application interactive connectée à l'analyse SQL (Segmentation RFM, Rétention et Chiffre d'affaires)."
)


# Fonction pour se connecter à la base de données SQLite et exécuter une requête
@st.cache_data
def load_data(query):
  # Remplacez 'olist.db' par le nom de votre fichier de base de données si nécessaire
  conn = sqlite3.connect("olist.db")
  df = pd.read_sql_query(query, conn)
  conn.close()
  return df


# Menu latéral pour naviguer entre les sections
menu = st.sidebar.selectbox(
    "Navigation",
    ["Accueil & Contexte", "Chiffre d'Affaires Mensuel", "Segmentation RFM"],
)

if menu == "Accueil & Contexte":
  st.header("Bienvenue sur le dashboard d'analyse Olist !")
  st.write(
      "Ce projet analyse une marketplace e-commerce brésilienne à travers"
      " différentes requêtes SQL optimisées."
  )
  st.info(
      "Utilisez le menu à gauche pour explorer le chiffre d'affaires et la"
      " segmentation RFM des clients."
  )

elif menu == "Chiffre d'Affaires Mensuel":
  st.header("📈 Évolution du Chiffre d'Affaires Mensuel")
  try:
    # Requête similaire à votre fichier 03_ca_mensuel.sql
    query_ca = """
        SELECT 
            strftime('%Y-%m', o.order_purchase_timestamp) AS mois,
            SUM(p.payment_value) AS chiffre_affaires,
            COUNT(DISTINCT o.order_id) AS nombre_commandes
        FROM orders o
        JOIN order_payments p ON o.order_id = p.order_id
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

      st.subheader("Données brutes")
      st.dataframe(df_ca)
    else:
      st.warning(
          "Aucune donnée trouvée. Assurez-vous que le fichier de base de"
          " données 'olist.db' est bien présent dans le dépôt avec les tables"
          " nécessaires."
      )
  except Exception as e:
    st.error(
        f"Erreur lors du chargement des données (Vérifiez si la base olist.db"
        f" est bien présente) : {e}"
    )

elif menu == "Segmentation RFM":
  st.header("🎯 Segmentation RFM des Clients")
  st.markdown(
      "Répartition des clients selon leur Récence, Fréquence et Montant."
  )
  try:
    # Exemple de requête pour la segmentation (basée sur vos scripts RFM)
    query_rfm = """
        SELECT 
            customer_unique_id,
            MAX(order_purchase_timestamp) AS derniere_commande,
            COUNT(order_id) AS frequence,
            SUM(payment_value) AS montant
        FROM (
            SELECT o.customer_unique_id, o.order_id, o.order_purchase_timestamp, p.payment_value
            FROM orders o
            JOIN order_payments p ON o.order_id = p.order_id
            WHERE o.order_status = 'delivered'
        )
        GROUP BY customer_unique_id
        LIMIT 1000;
        """
    df_rfm = load_data(query_rfm)
    if not df_rfm.empty:
      st.dataframe(df_rfm)
    else:
      st.warning("Données RFM non disponibles.")
  except Exception as e:
    st.error(
        f"Erreur lors de l'exécution de la requête RFM : {e}"
    )

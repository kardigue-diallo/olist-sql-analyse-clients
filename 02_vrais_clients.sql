SELECT COUNT(*) AS nb_commandes,
       COUNT(DISTINCT customer_unique_id) AS nb_vrais_clients
FROM olist_customers_dataset;
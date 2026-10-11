WITH commandes AS (
    SELECT c.customer_unique_id,
           strftime('%Y-%m', o.order_purchase_timestamp) AS mois_commande
    FROM olist_orders_dataset o
    JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
    WHERE o.order_status = 'delivered'
),
activite AS (
    SELECT customer_unique_id,
           mois_commande,
           MIN(mois_commande) OVER (PARTITION BY customer_unique_id) AS cohorte
    FROM commandes
),
decalages AS (
    SELECT customer_unique_id,
           cohorte,
           (CAST(substr(mois_commande, 1, 4) AS INTEGER) - CAST(substr(cohorte, 1, 4) AS INTEGER)) * 12
           + (CAST(substr(mois_commande, 6, 2) AS INTEGER) - CAST(substr(cohorte, 6, 2) AS INTEGER)) AS decalage_mois
    FROM activite
)
SELECT cohorte,
       COUNT(DISTINCT CASE WHEN decalage_mois = 0 THEN customer_unique_id END) AS taille_cohorte,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN decalage_mois = 1 THEN customer_unique_id END)
             / COUNT(DISTINCT CASE WHEN decalage_mois = 0 THEN customer_unique_id END), 2) AS pct_retour_m1,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN decalage_mois = 3 THEN customer_unique_id END)
             / COUNT(DISTINCT CASE WHEN decalage_mois = 0 THEN customer_unique_id END), 2) AS pct_retour_m3,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN decalage_mois = 6 THEN customer_unique_id END)
             / COUNT(DISTINCT CASE WHEN decalage_mois = 0 THEN customer_unique_id END), 2) AS pct_retour_m6
FROM decalages
WHERE cohorte BETWEEN '2017-01' AND '2018-02'
GROUP BY cohorte
ORDER BY cohorte;
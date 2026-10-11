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
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM segments), 2) AS pct_clients,
       ROUND(SUM(montant_total), 2) AS ca_segment,
       ROUND(100.0 * SUM(montant_total) / (SELECT SUM(montant_total) FROM segments), 2) AS pct_ca
FROM segments
GROUP BY segment
ORDER BY ca_segment DESC;
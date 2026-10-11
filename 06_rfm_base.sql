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
)
SELECT b.customer_unique_id,
       CAST(julianday((SELECT date_ref FROM ref)) - julianday(MAX(b.order_purchase_timestamp)) AS INTEGER) AS recence_jours,
       COUNT(DISTINCT b.order_id) AS frequence,
       ROUND(SUM(b.montant_commande), 2) AS montant_total
FROM base b
GROUP BY b.customer_unique_id
ORDER BY montant_total DESC
LIMIT 20;
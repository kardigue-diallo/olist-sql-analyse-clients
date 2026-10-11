SELECT strftime('%Y-%m', o.order_purchase_timestamp) AS mois,
       COUNT(DISTINCT o.order_id) AS nb_commandes,
       ROUND(SUM(i.price), 2) AS chiffre_affaires,
       ROUND(SUM(i.price) / COUNT(DISTINCT o.order_id), 2) AS panier_moyen
FROM olist_orders_dataset o
JOIN olist_order_items_dataset i ON o.order_id = i.order_id
WHERE o.order_status = 'delivered'
GROUP BY mois
ORDER BY mois;
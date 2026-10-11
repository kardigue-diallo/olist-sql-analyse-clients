SELECT COUNT(DISTINCT o.order_id) AS nb_commandes_livrees,
       ROUND(SUM(i.price), 2) AS ca_total
FROM olist_orders_dataset o
JOIN olist_order_items_dataset i ON o.order_id = i.order_id
WHERE o.order_status = 'delivered';
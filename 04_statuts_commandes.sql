SELECT order_status,
       COUNT(*) AS nb_commandes,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM olist_orders_dataset), 2) AS pourcentage
FROM olist_orders_dataset
GROUP BY order_status
ORDER BY nb_commandes DESC;
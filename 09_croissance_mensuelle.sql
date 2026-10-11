WITH ca_mensuel AS (
    SELECT strftime('%Y-%m', o.order_purchase_timestamp) AS mois,
           ROUND(SUM(i.price), 2) AS chiffre_affaires
    FROM olist_orders_dataset o
    JOIN olist_order_items_dataset i ON o.order_id = i.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY mois
)
SELECT mois,
       chiffre_affaires,
       LAG(chiffre_affaires) OVER (ORDER BY mois) AS ca_mois_precedent,
       ROUND(100.0 * (chiffre_affaires - LAG(chiffre_affaires) OVER (ORDER BY mois))
             / LAG(chiffre_affaires) OVER (ORDER BY mois), 2) AS croissance_pct
FROM ca_mensuel
WHERE mois BETWEEN '2017-01' AND '2018-08'
ORDER BY mois;
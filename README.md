# Segmentation client et analyse de rétention : e-commerce Olist (SQL)

Analyse d'une marketplace brésilienne réalisée **uniquement en SQL** (SQLite) : segmentation RFM, rétention par cohortes et croissance mensuelle du chiffre d'affaires.

L'objectif est de répondre à trois questions business : qui sont les meilleurs clients, qui est en train de partir, et combien de clients reviennent acheter.

## Données

- Source : [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/) (Kaggle), licence CC BY-NC-SA 4.0.
- 9 tables liées : commandes, clients, lignes de commande, paiements, avis, produits, vendeurs, géolocalisation, traduction des catégories.
- Volume : 99 441 commandes, 112 650 lignes de commande, 96 096 clients uniques, de 2016 à 2018.
- Les fichiers CSV et la base `olist.db` ne sont pas inclus dans ce dépôt (taille et licence). Pour reproduire l'analyse, téléchargez le dataset sur Kaggle et importez les 9 CSV dans SQLite (DB Browser for SQLite : *Fichier > Importer > Table depuis un fichier CSV*, avec « Tables distinctes » coché).

## Outils

SQLite, DB Browser for SQLite. Notions SQL utilisées : jointures multi-tables, agrégations, CTE (`WITH`), fonctions de fenêtrage (`NTILE`, `LAG`, `MIN() OVER`), `CASE`, sous-requêtes, index.

## Structure du dépôt

| Fichier | Contenu |
|---|---|
| `00_index.sql` | Index pour accélérer les jointures |
| `01_verification_import.sql` | Contrôle du nombre de lignes de chaque table |
| `02_vrais_clients.sql` | Commandes vs clients réels |
| `03_ca_mensuel.sql` | Chiffre d'affaires et panier moyen par mois |
| `04_statuts_commandes.sql` | Répartition des statuts de commande |
| `05_controle_ca.sql` | Contrôle de cohérence de la jointure |
| `06_rfm_base.sql` | Récence, fréquence, montant par client |
| `07_rfm_segments.sql` | Scores et segments RFM |
| `08_cohortes_retention.sql` | Rétention par cohortes mensuelles |
| `09_croissance_mensuelle.sql` | Croissance mensuelle avec `LAG()` |

## Choix méthodologiques

- **Vrais clients.** `customer_id` change à chaque commande ; seul `customer_unique_id` identifie une personne. Utiliser le premier aurait compté chaque commande comme un nouveau client (99 441 commandes pour 96 096 clients réels).
- **Commandes livrées uniquement.** Elles représentent 97,02 % des commandes (96 478). Les commandes annulées ou indisponibles n'ont généré aucun revenu réel.
- **Chiffre d'affaires** = somme des prix des articles, hors frais de port. Total sur les commandes livrées : 13 221 498,11 (reals brésiliens).
- **Date de référence de la récence** = date de la dernière commande du dataset, et non la date du jour, sinon toutes les récences seraient d'environ huit ans.
- **Fréquence : pas de `NTILE`.** Plus de 95 % des clients n'ont acheté qu'une fois ; découper en cinq groupes des clients identiques serait arbitraire. Règle retenue : 2 commandes ou plus = client fidèle.
- **Seuils des segments.** Les règles du `CASE` (scores 4-5 = récent ou gros montant, scores 1-2 = ancien ou faible montant) sont des choix de ma part, pas une vérité statistique.
- **Performance.** Une première version de la requête de cohortes (auto-jointure) dépassait 10 minutes. Après ajout d'index et remplacement de l'auto-jointure par `MIN() OVER (PARTITION BY ...)`, elle s'exécute en environ 4 secondes.

## Résultats

### Segmentation RFM (93 358 clients avec au moins une commande livrée)

| Segment | Clients | % clients | CA | % du CA |
|---|---|---|---|---|
| Gros acheteurs récents | 14 519 | 15,55 % | 3 877 678 | 29,33 % |
| À risque (gros montant) | 13 746 | 14,72 % | 3 806 579 | 28,79 % |
| Occasionnels | 18 067 | 19,35 % | 2 348 240 | 17,76 % |
| Perdus | 22 610 | 24,22 % | 1 259 040 | 9,52 % |
| Nouveaux clients | 21 615 | 23,15 % | 1 201 552 | 9,09 % |
| Fidèles actifs | 1 813 | 1,94 % | 484 852 | 3,67 % |
| Fidèles endormis | 988 | 1,06 % | 243 556 | 1,84 % |

- Seuls **3 %** des clients (2 801) ont commandé plus d'une fois.
- Le segment **« à risque »** représente 14,7 % des clients et 28,8 % du chiffre d'affaires : ce sont des clients à fort montant qui ne sont pas revenus depuis longtemps, cible naturelle d'une campagne de réactivation.
- Les « gros montant » pèsent lourd en partie par construction (définis comme les 40 % de clients qui dépensent le plus). L'information utile est le croisement avec la récence.

### Rétention par cohortes

Sur 14 cohortes mensuelles (janvier 2017 à février 2018), moins de 1 % des nouveaux clients repassent commande à 1, 3 ou 6 mois. La marketplace vit surtout d'acheteurs uniques. Les effectifs de retour sont très faibles (quelques dizaines de personnes par cohorte), donc les variations d'une cohorte à l'autre ne sont pas interprétables. La cohorte de novembre 2017 est la plus grosse (7 060 nouveaux clients), ce qui pourrait refléter un effet Black Friday (hypothèse, non démontrée par ces données).

### Croissance du chiffre d'affaires

Le chiffre d'affaires mensuel passe de 111 798 en janvier 2017 à 481 605 en juillet 2017. La croissance est très forte au démarrage (+109,5 % en février 2017, +53,4 % en mars 2017) puis irrégulière. À partir de mars 2018 (+15,4 %), le chiffre d'affaires se stabilise entre environ 840 000 et 980 000 par mois, avec des variations mensuelles comprises entre -12,4 % et +2,1 %.

## Limites

- Le dataset couvre 2016-2018 : les premiers et derniers mois sont incomplets, d'où un filtre sur les cohortes.
- L'absence de novembre 2016 dans les commandes livrées est une particularité des données.
- L'analyse est descriptive : elle ne prédit pas le comportement futur des clients.

## 🚀 Application en Direct

Vous pouvez tester le tableau de bord interactif complet déployé sur Streamlit Cloud :
👉 **[Accéder au Dashboard Olist Analytics](https://olist-sql-analyse-clients-spxwv9ukb9mxsh89patmwf.streamlit.app)**

## Pistes d'amélioration

- Ajouter l'analyse des avis clients (note moyenne par segment).
- Croiser la satisfaction (avis) et le retour d'achat.
- Visualiser les résultats dans un dashboard (Streamlit ou Power BI).

## Auteur

Kardigue Diallo : [GitHub](https://github.com/kardigue-diallo) · [LinkedIn](https://www.linkedin.com/in/kardigue-diallo) · [Kaggle](https://www.kaggle.com/kardiguediallo)

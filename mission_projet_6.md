# Étude de faisabilité — Moteur de classification de catégories produit  
**Entreprise** : *Place de marché*  
*(logo entreprise place de marché)*

---

## Contexte  
Vous êtes Data Scientist au sein de l’entreprise **Place de marché**, qui souhaite lancer une marketplace e-commerce anglophone.  
Sur cette marketplace, des vendeurs publient des articles (photo + description). L’attribution actuelle des catégories est manuelle (peu fiable) et le volume d’articles est encore faible. Pour améliorer l’expérience vendeur/acheteur et permettre un passage à l’échelle, il est nécessaire d’automatiser l’attribution des catégories.

Linda (Lead Data Scientist) demande une étude de faisabilité d’un moteur de classification des articles à partir **du texte (anglais)** et **de l’image**.

---

## Objectifs de la mission (résumé)  
1. Étudier la faisabilité d’un moteur automatique d’attribution de catégorie à partir d’une **image + description**.  
2. Comparer et extraire features image et texte avec plusieurs approches.  
3. Visualiser en 2D les produits (points colorés selon la catégorie réelle) et analyser la possibilité de regrouper automatiquement les produits par catégorie.  
4. Quantifier la similarité entre catégories réelles et clusters obtenus (mesure numérique pour confirmer l’analyse visuelle).  
5. Mettre en place une classification supervisée basée sur les images (avec data augmentation).  
6. Tester la collecte de produits « champagne » via l’API OpenFoodFacts et produire un CSV des 10 premiers produits.  
7. Produire un support de présentation (≤ 30 slides, PDF) documentant la démarche et les résultats.

---

## Pièces jointes fournies
- **PJ 1** : Jeu de données d’articles (images + descriptions + catégories).  
- **PJ 2** : Notebook d’extraction de features d’images et d’étude de faisabilité.  
- Notebook d’exemple de classification supervisée d’images (pour la suite).  
- Documentation / tutoriel OpenFoodFacts (API, sans inscription).

> *Nota Bene* : Linda précise qu’il n’y a **aucune contrainte de propriété intellectuelle** sur les données/images.

---

## Étapes demandées (détaillées)

### 1. Prétraitement des données
- Nettoyage textes (lowercase, suppression ponctuation, tokenisation, stop-words, lemmatisation/stemming si pertinent).  
- Vérification corrélations champ manquant / duplicatas / images corrompues.  
- Standardisation images (resize, normalisation pixel, vérification ratio / orientation).

### 2. Extraction de features — images
- Méthodes classiques de features locaux : **SIFT / ORB / SURF** (bag-of-visual-words possible).  
- Approche deep : **CNN + Transfer Learning** (ex. ResNet/Inception/EfficientNet → features intermédiaires).

### 3. Extraction de features — texte
- Bag-of-words : comptage simple (CountVectorizer).  
- TF-IDF.  
- Embeddings classiques : **Word2Vec** (ou Glove / FastText) → vecteur phrase (avg / pooling).  
- Embeddings contextuels : **BERT** (sentence embeddings via pooling ou sentence-transformers).  
- **USE (Universal Sentence Encoder)**.

### 4. Réduction de dimension & visualisation
- Réduction à **2 dimensions** (PCA / t-SNE / UMAP) pour projeter les produits.  
- Visualiser points 2D colorés selon la **catégorie réelle** (faciliter l’analyse visuelle des regroupements).

### 5. Analyse visuelle & conclusion de faisabilité
- Observer regroupements par catégorie : cohérence, chevauchements, sous-groupes.  
- Évaluer si texte et/ou image suffisent (ou combinaison multimodale) pour séparer les catégories.

### 6. Mesure quantitative
- Segmentation non supervisée (k-means, GMM, DBSCAN, etc.) → obtenir clusters.  
- Mesures de similarité entre catégories réelles et clusters : **ARI (Adjusted Rand Index)**, **AMI (Adjusted Mutual Info)**, **Homogeneity / Completeness / V-measure**, **NMI**.  
- Comparer performances selon features (image only, text only, multimodal concaténée / late fusion).

---

## Suite de la mission (mail de Linda — tâches additionnelles)

### A. Classification supervisée d’images
- Construire un pipeline de classification supervisée basé sur images.  
- **Data augmentation** (rotations, flips, zoom, translation, bruit, éclairage, etc.) pour améliorer généralisation.  
- Essayer plusieurs backbones (transfer learning) et fine-tuning.  
- Mesures à fournir : accuracy, precision, recall, F1 par classe, matrice de confusion, ROC AUC si binaire/multi-étiquette adapté.

### B. Extension gamme produit : collecte “champagne”
- Tester la collecte de produits contenant le mot **“champagne”** via l’API OpenFoodFacts (ou autre API fournie).  
- Produire un script / notebook Python qui :
  - Requête l’API pour rechercher produits contenant “champagne”.  
  - Extrait les **10 premiers** produits et sauvegarde dans un fichier **`.csv`** avec colonnes :
    - `foodId`, `label`, `category`, `foodContentsLabel`, `image`

  Exemple d’en-tête CSV :
  ```csv
  foodId,label,category,foodContentsLabel,image

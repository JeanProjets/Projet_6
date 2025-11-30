# Livrables et Soutenance

## 📦 Livrables

### Description des Livrables

Vous devez remettre **4 livrables** structurés de la manière suivante :

#### **Livrable 1: Notebooks de Prétraitement et Feature Extraction**

Un ou plusieurs notebooks (ou fichiers `.py`) contenant :
- Les **fonctions de prétraitement** des données textes et images
- Les **extractions de features** pour les textes et images
- Les **résultats de l'étude de faisabilité** :
  - Graphiques et visualisations (2D avec t-SNE ou PCA)
  - Mesures de similarité entre catégories réelles et clusters obtenus
  - Analyses visuelles et quantitatives

**Nom du fichier**: `Nom_Prénom_1_notebook_pretraitement_feature_extraction_faisabilite_mmaaaa`

*Exemple*: `Dupont_Jean_1_notebook_pretraitement_feature_extraction_faisabilite_012024`

---

#### **Livrable 2: Notebook de Classification Supervisée**

Un notebook contenant :
- L'implémentation du modèle de **classification supervisée des images**
- Les approches testées (architectures CNN, hyperparamètres)
- Les résultats d'entraînement et d'évaluation
- Les métriques de performance (accuracy, precision, recall, F1-score)
- Les visualisations des résultats (matrices de confusion, courbes d'apprentissage, etc.)

**Nom du fichier**: `Nom_Prénom_2_notebook_classification_mmaaaa`

*Exemple*: `Dupont_Jean_2_notebook_classification_012024`

---

#### **Livrable 3: Script Python de Test d'API**

Un script Python (notebook ou fichier `.py`) contenant :
- Le **test complet de l'API** pour l'extraction de données
- L'**extraction des produits** (champagne ou autre catégorie fine food)
- Les résultats structurés en format **CSV**

Le fichier CSV doit inclure les colonnes :
- `foodId`: Identifiant unique du produit
- `label`: Nom/description du produit
- `category`: Catégorie du produit
- `foodContentsLabel`: Information de contenu/ingrédients
- `image`: URL ou données de l'image du produit

**Nom du fichier**: `Nom_Prénom_3_script_Python_mmaaaa`

*Exemple*: `Dupont_Jean_3_script_Python_012024`

---

#### **Livrable 4: Présentation de Soutenance**

Un support de **présentation pour la soutenance** détaillant l'ensemble du travail réalisé :
- Format: **PowerPoint ou équivalent, sauvegardé en PDF**
- **Maximum 30 slides**
- Contenu requis:
  - L'étude de faisabilité
  - La classification supervisée
  - Le test de l'API

**Nom du fichier**: `Nom_Prénom_4_presentation_mmaaaa`

*Exemple*: `Dupont_Jean_4_presentation_012024`

---

### 📁 Consignes de Dépôt

1. **Créez un dossier zip** nommé : `Titre_du_projet_nom_prénom`

2. **Placez tous les livrables** dans ce dossier avec les noms exacts spécifiés ci-dessus

3. **Déposez le dossier zip** sur la plateforme

**Exemple de structure complète** :
```
Titre_du_projet_Dupont_Jean/
├── Dupont_Jean_1_notebook_pretraitement_feature_extraction_faisabilite_012024.ipynb
├── Dupont_Jean_2_notebook_classification_012024.ipynb
├── Dupont_Jean_3_script_Python_012024.py
├── Dupont_Jean_4_presentation_012024.pdf
└── produits_extraits.csv
```

---

## 🎤 Soutenance

### Format et Durée

- **Format**: Visioconférence
- **Durée totale**: **30 minutes**
- **Support**: Présentation PDF (Livrable 4)

### Rôle du Rôle de l'Évaluateur

L'évaluateur jouera le rôle de **Linda**, votre client/manager qui vous challengera sur vos choix techniques et méthodologiques.

---

### 📋 Agenda de la Soutenance

#### **Présentation (20 minutes)**

##### 1️⃣ **Rappel de la Problématique et Présentation du Jeu de Données** (3 minutes)
- Contexte du projet (e-commerce "Place de marché")
- Problématique de classification manuelle des produits
- Description du jeu de données utilisé
- Objectifs généraux du projet

##### 2️⃣ **Prétraitements, Extractions de Features et Résultats de Faisabilité** (10 minutes)
- Explications détaillées des approches de **prétraitement** :
  - Text: nettoyage, tokenization, normalisation
  - Images: redimensionnement, normalisation
- Méthodes d'**extraction de features** utilisées :
  - Text: Bag-of-Words, TF-IDF, Word2Vec, BERT, USE
  - Images: SIFT/SURF/ORB, Transfer Learning CNN
- Résultats de l'**étude de faisabilité** :
  - Visualisations 2D (t-SNE, PCA)
  - Mesures de similarité et clustering
  - Interprétations et conclusions sur la faisabilité

##### 3️⃣ **Résultats de la Classification Supervisée** (5 minutes)
- Architecture et stratégies du modèle CNN
- Techniques d'augmentation de données utilisées
- Métriques de performance (accuracy, precision, recall, F1-score)
- Visualisations (matrices de confusion, courbes d'apprentissage)
- Conclusions sur la performance du modèle

##### 4️⃣ **Présentation du Test de l'API** (2 minutes)
- Description de l'API utilisée (Edamam ou OpenFood Facts)
- Processus d'extraction des produits
- Structure du fichier CSV généré
- Nombre de produits extraits et pertinence des résultats

---

#### **Discussion** (5 minutes)

L'évaluateur, jouant le rôle de **Linda**, vous posera des questions et vous challengera sur :
- Vos **choix de prétraitement** et leur justification
- Vos **méthodes de feature extraction** : pourquoi ces approches ?
- Les **résultats de faisabilité** : qu'en déduisez-vous ?
- Votre **architecture CNN** et les décisions d'hyperparamètres
- Les **performances du modèle** : comment les interprétez-vous ?
- L'**extraction d'API** : avez-vous rencontré des défis ?

**Conseils** :
- Soyez prêts à justifier vos choix techniques
- Montrez votre compréhension des concepts
- Écoutez attentivement les questions et répondez de façon précise
- Proposez des améliorations ou des perspectives futures si pertinent

---

#### **Débriefing** (5 minutes)

À la fin de la soutenance, l'évaluateur **arrêtera de jouer le rôle de Linda** pour un débriefing constructif :
- Retours sur votre présentation
- Points forts et axes d'amélioration
- Discussions ouvertes sur vos apprentissages
- Questions de clarification

---

## ✅ Checklist de Préparation

Avant la soutenance, assurez-vous que :

- [ ] Tous les 4 livrables sont complétés et nommés correctement
- [ ] Le notebook de prétraitement inclut toutes les visualisations et analyses
- [ ] Le notebook de classification contient les résultats finaux et les métriques
- [ ] Le script d'API est fonctionnel et génère un CSV complet
- [ ] La présentation PDF contient maximum 30 slides et couvre tous les points requis
- [ ] Vous avez pratiqué la présentation et pouvez la faire en 20 minutes
- [ ] Vous comprenez chaque choix technique que vous avez fait
- [ ] Vous pouvez expliquer les concepts clés (prétraitement, features, classification)
- [ ] Vous êtes préparés aux questions challengeantes

---

## 💡 Conseils pour la Réussite

1. **Structurez votre présentation de façon logique** : problème → solution → résultats
2. **Utilisez des visualisations claires** : les graphiques parlent plus que les paroles
3. **Pratiquez votre timing** : 3 min + 10 min + 5 min + 2 min = 20 min
4. **Soyez prêts à zoomer** sur des détails techniques si demandé
5. **Montrez votre pensée critique** : analysez vos résultats, pas juste présentez-les
6. **Restez calme pendant la discussion** : c'est normal d'être challengé
7. **Documentez votre code** : commentaires clairs et docstrings dans vos scripts

---

**Bonne chance pour votre soutenance! 🚀**

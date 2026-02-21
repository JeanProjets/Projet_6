# 🎙️ Script de Soutenance Détaillé (Durée cible : 20 min)

---

## 1. Introduction & Contexte (0:00 - 0:02)
"Bonjour à tous. Je suis ravi de vous présenter aujourd'hui les résultats de ma mission pour la marketplace e-commerce. Notre client fait face à un défi de croissance : avec des milliers de nouveaux articles chaque jour, l'attribution manuelle des catégories par les vendeurs est devenue une source d'erreurs et de frustration. Mon rôle a été de concevoir un système automatisé de classification, capable d'analyser à la fois le descriptif textuel et l'image du produit."

---

## 2. Présentation du Dataset (0:02 - 0:04)
"Pour ce projet, nous avons utilisé un échantillon du catalogue Flipkart. Ce dataset est composé de 1050 produits. Un point crucial pour la fiabilité de nos futurs modèles est que le jeu de données est parfaitement équilibré : nous avons 150 articles pour chacune des 7 catégories. Cela nous prémunit contre les biais de classification où un modèle pourrait favoriser une classe sur-représentée."

---

## 3. Prétraitement NLP : Pourquoi la Lemmatisation ? (0:04 - 0:07)
"Entrons dans la technique avec le traitement du texte. J'ai mis en place un pipeline de nettoyage classique : suppression des balises HTML, de la ponctuation et des 'stop-words'. 
Mais j'aimerais m'attarder sur le choix entre le Stemming et la Lemmatisation. Là où le stemming coupe simplement la fin des mots, la lemmatisation utilise un dictionnaire pour ramener le mot à sa forme canonique. J'ai choisi la lemmatisation car elle préserve mieux le sens sémantique, ce qui est vital pour différencier des produits techniques."

---

## 4. Prétraitement Vision : Préparer le CNN (0:07 - 0:09)
"Côté image, le défi est la standardisation. Les réseaux de neurones convolutionnels imposent une taille d'entrée fixe. J'ai donc redimensionné tous les visuels en 224x224 pixels. J'ai également appliqué une normalisation des pixels. En ramenant les valeurs de 0 à 255 vers une échelle plus petite, on aide l'optimiseur à converger beaucoup plus rapidement lors de l'entraînement."

---

## 5. Extraction de Features : De TF-IDF aux Transformers (0:09 - 0:12)
"Pour transformer le texte en vecteurs, j'ai testé plusieurs méthodes. 
Le TF-IDF est excellent pour capter la rareté des mots : un mot comme 'LCD' apparaîtra peu souvent mais sera très discriminant pour la catégorie 'Computers'.
Cependant, pour capter le contexte, je suis passé aux Embeddings avec BERT et l'Universal Sentence Encoder. Ces modèles 'comprennent' que 'fauteuil' et 'siège' partagent une proximité sémantique, là où les méthodes fréquentielles échouent."

---

## 6. SIFT et Bag of Visual Words (0:12 - 0:14)
"Pour l'image, j'ai d'abord testé l'approche classique SIFT. C'est un algorithme qui détecte des points d'intérêt (angles, bords). J'ai ensuite utilisé une technique de 'Bag of Visual Words' : on groupe les milliers de descripteurs SIFT en 'clusters' pour créer un dictionnaire de formes. Chaque image est alors définie par la fréquence de ces formes. C'est une approche robuste mais gourmande en calcul."

---

## 7. Deep Learning : La puissance du Transfer Learning (0:14 - 0:16)
"L'approche la plus performante a été le Transfer Learning. J'ai utilisé VGG16, un modèle déjà entraîné sur des millions d'images. Plutôt que de repartir de zéro, j'utilise sa capacité à extraire des formes complexes. J'ai extrait les features de la dernière couche de convolution. Comme on le voit sur le graphique t-SNE, cette méthode produit les clusters les plus nets, avec un score ARI de 0.69, ce qui est très élevé pour du clustering non supervisé."

---

## 8. Classification Supervisée : Résultats (0:16 - 0:18)
"Fort de ces résultats, j'ai entraîné un classifieur supervisé. Pour éviter l'overfitting, j'ai utilisé la 'Data Augmentation' : en faisant pivoter ou en zoomant sur les images, on crée virtuellement de nouveaux exemples. 
Le modèle final atteint 83.3% d'accuracy sur le test set. L'analyse par classe montre que nous sommes excellents sur les montres, mais que nous avons encore des marges de progression sur la distinction entre décoration et ameublement."

---

## 9. API et Conclusion (0:18 - 0:20)
"Enfin, j'ai intégré une brique de collecte de données via l'API OpenFood Facts. Ce script permet d'automatiser l'ajout de nouveaux produits comme le Champagne, en récupérant les ingrédients et les visuels. 
Pour conclure, ce projet valide la faisabilité d'une classification hybride. Pour une mise en production, je recommanderais un modèle multimodal 'late-fusion' qui ferait la moyenne des prédictions du texte et de l'image. Merci de m'avoir écouté."

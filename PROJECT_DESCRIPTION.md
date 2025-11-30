# Automated Product Classification for E-Commerce Marketplace

## 📋 Project Overview

This project aims to develop and implement a **multimodal machine learning system** that automatically classifies e-commerce product articles using both text descriptions (in English) and product images. The system is designed for "Place de marché," an English-speaking e-commerce marketplace where sellers post products with photos and descriptions.

### 🎯 Business Problem

Currently, product category attribution is performed **manually by sellers**, which is:
- **Unreliable**: Inconsistent and error-prone categorization
- **Not scalable**: Cannot handle growing volume of articles
- **Poor UX**: Creates friction for both sellers (difficult to list products) and buyers (difficult to find products)

**Goal**: Automate the product category attribution process to improve user experience and enable platform scalability.

---

## 🎓 Learning Objectives

Through this project, you will learn to:

1. **Text Preprocessing & Feature Extraction**
   - Clean and structure raw textual data for ML algorithms
   - Implement multiple text encoding approaches
   - Handle natural language data effectively

2. **Image Preprocessing & Feature Extraction**
   - Prepare images for machine learning models
   - Extract visual features using traditional and deep learning methods
   - Optimize image data for computer vision tasks

3. **Multimodal Data Integration**
   - Adapt preprocessing approaches to different data types
   - Combine text and image features effectively
   - Create unified representations of multimodal data

4. **Dimensionality Reduction & Visualization**
   - Project high-dimensional data to 2D for visualization
   - Analyze clustering patterns and data distribution
   - Assess model feasibility through visual inspection

5. **Supervised Image Classification**
   - Implement data augmentation strategies
   - Train CNN models on custom datasets
   - Evaluate and optimize classification performance

6. **API Integration & Data Collection**
   - Query external APIs (Edamam, OpenFood Facts)
   - Process and structure API responses
   - Build automated data pipelines

### 💼 Why These Skills Matter for Your Career

These competencies are crucial for AI/ML engineers:

- **Data Preprocessing Expertise**: Essential for converting raw, unstructured data into formats that ML algorithms can process. Good preprocessing directly impacts model performance.

- **Versatility with Multiple Data Types**: Modern AI systems work with diverse data sources (text, images, tabular data, structured/unstructured). This skill is increasingly in demand.

- **Multimodal Learning**: Combining multiple data modalities to create more robust and comprehensive models is a key frontier in AI research and industry applications.

- **Supervised Image Classification**: Fundamental for numerous computer vision applications:
  - Object recognition
  - Quality control in manufacturing
  - Content analysis for social media
  - Medical image analysis

- **Precision and Efficiency**: In production environments, model accuracy and computational efficiency often determine project success.

---

## 📊 Project Structure

### Phase 1: Feasibility Study - Text & Image Analysis

#### 1.1 Data Preprocessing
- **Text Preprocessing**: Cleaning, tokenization, normalization of product descriptions
- **Image Preprocessing**: Resizing, normalization, quality checks

#### 1.2 Feature Extraction from Images

Two complementary approaches:

**A) Traditional Computer Vision Methods**
- **SIFT** (Scale-Invariant Feature Transform)
- **ORB** (Oriented FAST and Rotated BRIEF)
- **SURF** (Speeded-Up Robust Features)

*Purpose*: Extract keypoint-based features to capture local image structures

**B) Deep Learning Transfer Learning**
- **CNN Transfer Learning**: Leverage pre-trained convolutional neural networks (e.g., VGG, ResNet, InceptionV3)

*Purpose*: Extract high-level semantic features from images

#### 1.3 Feature Extraction from Text

Multiple complementary approaches to extract semantic meaning:

**A) Bag-of-Words Methods**
- Simple word count approach
- TF-IDF (Term Frequency-Inverse Document Frequency)

*Purpose*: Statistical representation of text importance

**B) Word & Sentence Embeddings (Classical)**
- **Word2Vec** (or alternative: GloVe, FastText)

*Purpose*: Dense vector representations capturing semantic relationships

**C) Contextual Embeddings**
- **BERT** (Bidirectional Encoder Representations from Transformers)

*Purpose*: Context-aware word representations considering surrounding words

**D) Sentence-Level Embeddings**
- **USE** (Universal Sentence Encoder)

*Purpose*: Direct sentence-level embeddings for semantic similarity

#### 1.4 Dimensionality Reduction & Visualization
- Reduce extracted features to 2D space (e.g., using t-SNE or PCA)
- Visualize products as colored points where color represents actual category
- **Goal**: Assess whether products of the same category naturally cluster together

#### 1.5 Feasibility Analysis
- **Visual Inspection**: Analyze clustering patterns in 2D visualization
- **Quantitative Validation**: Calculate similarity between:
  - Real product categories
  - Categories obtained from clustering algorithms (e.g., K-means)
- **Conclusion**: Determine if automated category classification is feasible

**Key Deliverable**: Demonstrate whether products can be automatically grouped by category based on text and image features

---

### Phase 2: Supervised Classification & Expansion

#### 2.1 Supervised Image Classification
- Implement CNN-based supervised classification model
- Train on labeled product images with known categories
- Fine-tune using transfer learning for better performance

#### 2.2 Data Augmentation
- Apply augmentation techniques to:
  - Increase training dataset size
  - Improve model robustness
  - Reduce overfitting risk
- Techniques: rotation, scaling, flipping, brightness adjustment, etc.

#### 2.3 Product Range Expansion - Fine Food Category
- **Objective**: Extend marketplace to include fine food products (e.g., champagne)
- **Data Source Options**:
  - **Edamam Food Database API**: https://developer.edamam.com/food-database-api
  - **OpenFood Facts API**: Free, no registration required (documentation provided)

#### 2.4 Automated Data Collection Pipeline
- Query APIs with search term "champagne"
- Extract and process top 10 results
- Structure data into CSV format with fields:
  - `foodId`: Unique product identifier
  - `label`: Product name/description
  - `category`: Product category
  - `foodContentsLabel`: Ingredient/content information
  - `image`: Product image URL or data

**Deliverable**: Python script/notebook for automated product extraction to CSV

#### 2.5 Project Documentation & Presentation
- Create comprehensive PDF presentation (maximum 30 slides)
- Include:
  - Project methodology and approach
  - Most relevant analysis results
  - Visual representations of findings
  - Model performance metrics
  - Conclusions and recommendations

**Deliverable**: Professional presentation documenting entire project workflow and results

---

## 📁 Data Sources

- **Primary Dataset**: Product articles with images and text descriptions (provided)
  - Link: https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Textimage+DAS+V2/Dataset+projet+pre%CC%81traitement+textes+images.zip

- **Reference Notebooks**:
  - Image feature extraction & feasibility study example
  - Supervised classification example
  - Links provided in project materials

- **APIs for Fine Food Data**:
  - Edamam Food Database API
  - OpenFood Facts API (no registration required)

---

## 🛠️ Technical Stack

### Expected Technologies & Libraries

**Data Processing**:
- pandas, NumPy
- scikit-learn

**Image Processing**:
- OpenCV
- PIL/Pillow

**Feature Extraction - Images**:
- OpenCV (SIFT, ORB, SURF)
- TensorFlow/Keras or PyTorch (CNN Transfer Learning)
- Pre-trained models (VGG, ResNet, Inception, etc.)

**Feature Extraction - Text**:
- NLTK or spaCy (preprocessing)
- scikit-learn (Bag-of-Words, TF-IDF)
- Gensim (Word2Vec)
- HuggingFace Transformers (BERT, USE)
- TensorFlow Hub (Universal Sentence Encoder)

**Dimensionality Reduction**:
- scikit-learn (PCA, t-SNE, UMAP)

**Clustering & Evaluation**:
- scikit-learn (K-means, clustering metrics)

**API Interaction**:
- requests library
- urllib

**Visualization**:
- Matplotlib, Seaborn, Plotly

**Documentation**:
- Jupyter Notebooks
- Markdown
- PDF generation tools

---

## ✅ Project Deliverables

### Phase 1:
1. ✓ Processed and cleaned text & image data
2. ✓ Feature extraction implementations (6 text methods + 2 image methods)
3. ✓ 2D visualization of product features colored by actual categories
4. ✓ Visual feasibility analysis with interpretation
5. ✓ Quantitative clustering similarity metrics

### Phase 2:
1. ✓ Supervised CNN image classification model
2. ✓ Data augmentation implementation
3. ✓ API-based data collection script/notebook
4. ✓ CSV file with extracted fine food products
5. ✓ Professional PDF presentation (≤30 slides)

---

## 📚 Key Concepts & Methods

### Text Analysis Methods Explained

| Method | Type | Pros | Cons |
|--------|------|------|------|
| **Bag-of-Words (Count)** | Statistical | Simple, interpretable | Ignores word order, context |
| **TF-IDF** | Statistical | Better than BOW, weights importance | Still ignores context |
| **Word2Vec** | Embedding | Captures semantics, word relationships | Static embeddings |
| **BERT** | Contextual Embedding | Context-aware, very powerful | Computationally expensive |
| **USE** | Sentence Embedding | Direct sentence-level, efficient | May lose fine-grained details |

### Image Analysis Methods Explained

| Method | Type | Pros | Cons |
|--------|------|------|------|
| **SIFT/SURF/ORB** | Keypoint Detection | Rotation/scale invariant, traditional | Handcrafted, computationally intensive |
| **CNN Transfer Learning** | Deep Learning | High-level semantics, pre-trained | Requires GPU, black-box |

---

## 🎯 Success Criteria

- ✓ Successfully preprocess text and image data
- ✓ Implement all required feature extraction methods
- ✓ Create clear, interpretable 2D visualizations
- ✓ Provide quantitative validation of feasibility
- ✓ Build working supervised classification model
- ✓ Collect data from external API successfully
- ✓ Present findings in professional manner

---

## 📝 Next Steps

1. **Review project requirements** thoroughly
2. **Set up development environment** with required libraries
3. **Download and explore datasets** to understand data structure
4. **Study reference notebooks** provided
5. **Begin Phase 1** with data preprocessing
6. **Progress through feature extraction** systematically
7. **Validate feasibility** with quantitative metrics
8. **Move to Phase 2** for supervised classification
9. **Integrate API data** collection
10. **Prepare final presentation**

---

## 📞 Resources & Support

- Review all reference materials and example notebooks
- Consult webinars and tutorials for SIFT implementation
- Refer to official API documentation for data collection
- Prepare questions for mentoring sessions

---

**Project Status**: Ready to commence

**Estimated Scope**: Comprehensive multimodal machine learning project with both exploratory and predictive components

**Impact**: Build a scalable, automated product classification system for e-commerce platform

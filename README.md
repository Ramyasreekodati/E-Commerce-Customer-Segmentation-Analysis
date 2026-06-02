# E-Commerce Customer Segmentation Analysis

## Project Overview

This project analyzes customer behavior for an e-commerce business to discover customer segments and predict customer satisfaction.

The workflow follows CRISP-DM:
- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment

## Business Problem

The business goal is to improve customer experience and retention by:
- identifying high-value and at-risk customer segments
- understanding drivers of satisfaction
- predicting satisfaction level for incoming customers

## Datasets

- `E-commerce Customer Behavior - Sheet1.csv` — original raw dataset
- `prepared_data.csv` — cleaned and feature-engineered dataset used for clustering
- `train_data.csv`, `test_data.csv` — split datasets used for supervised model training and evaluation
- `best_satisfaction_model.pkl` — exported trained Random Forest classification model
- `all_visuals.pdf` — consolidated report of all charts and visualizations (32 pages)

## Phase 1: Business Understanding

The project explores customer lifetime behavior and satisfaction, with three main objectives:
1. Segment customers into behavior-based groups
2. Identify which metrics drive satisfaction
3. Build a predictive classification model for satisfaction level

## Phase 2: Data Understanding

Exploratory data analysis examined:
- numerical distributions and outliers
- categorical distributions for membership and gender
- satisfaction levels across product categories, membership tiers, and demographic groups
- missing values and data quality issues
- correlations and multicollinearity

Key visual assets include:
- `business_overview.png`
- `missing_values_analysis.png`
- `correlation_heatmaps.png`
- `categorical_distributions.png`
- `satisfaction_by_membership.png`

## Phase 3: Data Preparation

Data preparation steps included:
- encoding categorical fields such as `Membership` and `Gender`
- engineering behavioral features such as `Spend_Per_Item`, `Engagement_Score`, and recency metrics
- standardizing key clustering features
- splitting the dataset into training (`train_data.csv`, 280 rows) and test (`test_data.csv`, 70 rows) sets

## Phase 4: Modeling

### Unsupervised Learning: Customer Segmentation

A K-Means clustering model was built using standardized features:
- `Total Spend_std`
- `Items Purchased_std`
- `Days Since Last Purchase_std`

Model selection:
- `K` evaluated across 2–8 clusters
- optimal value: **6 clusters** based on silhouette score
- silhouette scores by cluster count: 2=0.537, 3=0.5406, 4=0.5574, 5=0.6564, 6=0.7031, 7=0.6921, 8=0.6549

Cluster sizes:
- Cluster 0: 58 customers
- Cluster 1: 59 customers
- Cluster 2: 58 customers
- Cluster 3: 34 customers
- Cluster 4: 82 customers
- Cluster 5: 59 customers

Segment profiling identified groups like high spenders, frequent purchasers, and more price-sensitive or lower engagement customers.

Key clustering visuals:
- `optimal_k_clustering.png`
- `kmeans_pca_clusters.png`
- `cluster_profiles.png`

### Supervised Learning: Satisfaction Prediction

The classification objective predicts `Satisfaction_Encoded` using the prepared features.

Baseline model performance on the held-out test set:
- Logistic Regression: **100.00%**
- Random Forest: **98.57%**
- Gradient Boosting: **98.57%**
- Support Vector Machine: **82.86%**

Hyperparameter tuning for Random Forest produced:
- best parameters: `{'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 200}`
- best cross-validation accuracy: **99.29%**
- tuned model test accuracy: **100.00%**

Top features driving satisfaction according to the tuned Random Forest:
1. `Total Spend` (≈18.95%)
2. `Days Since Last Purchase` (≈18.04%)
3. `Discount Applied` (≈13.62%)
4. `Membership_Encoded` (≈11.03%)
5. `Items Purchased` (≈10.36%)

Important modeling visuals:
- `confusion_matrix_baseline.png`
- `feature_importance.png`

## Phase 5 & Phase 6: Evaluation and Deployment

The final notebook covers:
- classification evaluation
- confusion matrix and model report review
- business deployment recommendations
- saving and exporting the final model

Deployment notes:
- the trained Random Forest model is exported as `best_satisfaction_model.pkl`
- use the model to score new customers and target interventions for low-satisfaction segments
- monitor model performance over time and retrain as new customer behavior data arrives

## Key Insights

- High spend and recent purchase activity are the strongest predictors of customer satisfaction.
- Discounts and membership status also significantly influence satisfaction.
- Six customer segments were identified, suggesting differentiated marketing and retention strategies.
- The model is highly accurate on the current dataset, but should be validated on new data before production deployment.

## Visual Report

All chart output has been consolidated into a single file:
- `all_visuals.pdf` — 32 pages of plots

## How to Use This Repository

1. Open the Jupyter notebooks in order:
   - `CRISP_DM_Step1_Business_Understanding.ipynb`
   - `CRISP_DM_Step2_Data_Understanding.ipynb`
   - `CRISP_DM_Step3_Data_Preparation.ipynb`
   - `CRISP_DM_Step4_Modeling.ipynb`
   - `CRISP_DM_Step5_6_Evaluation_Deployment.ipynb`
2. Inspect the prepared datasets and visual files.
3. Use `best_satisfaction_model.pkl` for scoring new customer examples.

## Recommended Next Steps

- validate the model on new or external customer data
- add a production scoring pipeline for real-time customer satisfaction predictions
- use cluster profiles to personalize promotions and loyalty programs
- track how customer satisfaction shifts after marketing or pricing changes

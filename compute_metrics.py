import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

train = pd.read_csv('train_data.csv')
test = pd.read_csv('test_data.csv')
print('train shape', train.shape)
print('test shape', test.shape)
print('columns', train.columns.tolist()[:10], '...')

prepared = pd.read_csv('prepared_data.csv')
print('prepared shape', prepared.shape)
for col in ['Total Spend_std', 'Items Purchased_std', 'Days Since Last Purchase_std']:
    print(col, col in prepared.columns)

if all(col in prepared.columns for col in ['Total Spend_std', 'Items Purchased_std', 'Days Since Last Purchase_std']):
    X_cluster = prepared[['Total Spend_std', 'Items Purchased_std', 'Days Since Last Purchase_std']]
    scores = []
    ks = list(range(2, 9))
    for k in ks:
        km = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
        km.fit(X_cluster)
        scores.append(silhouette_score(X_cluster, km.labels_))
    best_k = ks[np.argmax(scores)]
    print('best_k', best_k)
    print('silhouette scores', list(zip(ks, [round(s, 4) for s in scores])))
    km = KMeans(n_clusters=best_k, init='k-means++', random_state=42, n_init=10)
    labels = km.fit_predict(X_cluster)
    print('cluster counts', pd.Series(labels).value_counts().sort_index().to_dict())
else:
    print('cluster columns missing')

X_train = train.drop(columns=['Satisfaction_Encoded'])
y_train = train['Satisfaction_Encoded']
X_test = test.drop(columns=['Satisfaction_Encoded'])
y_test = test['Satisfaction_Encoded']
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'Support Vector Machine': SVC(random_state=42)
}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    print(name, round(accuracy_score(y_test, y_test_pred) * 100, 2))

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
rf = RandomForestClassifier(random_state=42)
gs = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')
gs.fit(X_train, y_train)
print('grid best params', gs.best_params_)
print('grid best cv acc', round(gs.best_score_ * 100, 2))
final = gs.best_estimator_
y_pred = final.predict(X_test)
print('grid test acc', round(accuracy_score(y_test, y_pred) * 100, 2))
print('top 5 feature importances', sorted(zip(X_train.columns, final.feature_importances_), key=lambda x: -x[1])[:5])

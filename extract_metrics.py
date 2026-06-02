import json
from pathlib import Path
base = Path('.')
files = ['CRISP_DM_Step4_Modeling.ipynb', 'CRISP_DM_Step5_6_Evaluation_Deployment.ipynb']
keywords = ['KMeans', 'silhouette_score', 'n_clusters', 'n_cluster', 'RandomForest', 'accuracy_score', 'confusion_matrix', 'classification_report', 'cross_val', 'joblib', 'best_estimator_', 'GridSearch', 'RandomForestClassifier', 'accuracy']
for fname in files:
    print('---', fname)
    nb = json.loads((base / fname).read_text(encoding='utf-8'))
    printed = False
    for cell in nb['cells']:
        if cell['cell_type']=='code':
            text = ''.join(cell['source'])
            for line in text.splitlines():
                if any(kw in line for kw in keywords):
                    print(line)
                    printed = True
    if not printed:
        print('(no matches)')

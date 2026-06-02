import json
from pathlib import Path
base = Path('.')
files = [
    'CRISP_DM_Step1_Business_Understanding.ipynb',
    'CRISP_DM_Step2_Data_Understanding.ipynb',
    'CRISP_DM_Step3_Data_Preparation.ipynb',
    'CRISP_DM_Step4_Modeling.ipynb',
    'CRISP_DM_Step5_6_Evaluation_Deployment.ipynb'
]
keywords = ['accuracy', 'precision', 'recall', 'f1', 'roc', 'silhouette', 'elbow', 'score', 'cluster', 'segment', 'satisfaction', 'baseline', 'random forest', 'model', 'ROI', 'AUC']
for fname in files:
    path = base / fname
    nb = json.loads(path.read_text(encoding='utf-8'))
    print('---', fname)
    printed = False
    for cell in nb['cells']:
        if cell['cell_type'] in ('markdown', 'code'):
            text = ''.join(cell['source']).lower()
            for kw in keywords:
                if kw in text:
                    if not printed:
                        printed = True
                    for line in text.splitlines():
                        if kw in line:
                            print(line.strip())
    if not printed:
        print('(no keyword matches)')

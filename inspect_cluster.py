import json
from pathlib import Path
base = Path('.')
path = base / 'CRISP_DM_Step4_Modeling.ipynb'
nb = json.loads(path.read_text(encoding='utf-8'))
for i, cell in enumerate(nb['cells']):
    if cell['cell_type']=='code':
        text = ''.join(cell['source'])
        if 'X_cluster' in text or 'df_cluster' in text or 'cluster' in text.lower() and 'fit_transform' in text.lower():
            print('--- CELL', i)
            print(text)

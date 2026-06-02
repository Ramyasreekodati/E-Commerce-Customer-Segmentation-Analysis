import json
from pathlib import Path
base = Path('.')
path = base / 'CRISP_DM_Step4_Modeling.ipynb'
nb = json.loads(path.read_text(encoding='utf-8'))
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        text = ''.join(cell['source'])
        if 'K_range' in text or 'best_k' in text or 'GridSearchCV' in text or 'random forest' in text.lower() or 'classification_report' in text or 'confusion_matrix' in text:
            print('--- CELL', i)
            print(text)

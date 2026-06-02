import json
from pathlib import Path
base=Path('.')
path = base / 'CRISP_DM_Step4_Modeling.ipynb'
nb = json.loads(path.read_text(encoding='utf-8'))
for i, cell in enumerate(nb['cells']):
    if cell['cell_type']=='code':
        text=''.join(cell['source'])
        if 'X_train' in text or 'y_train' in text or 'train_test_split' in text or 'prepare' in text.lower() or 'feature' in text.lower() and 'importance' in text.lower():
            print('--- CELL', i)
            print(text)

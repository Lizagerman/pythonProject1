# utils.py

import json
import os
from typing import List, Dict, Any

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


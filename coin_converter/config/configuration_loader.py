"""
import yaml
from pathlib import Path

def load_config(caminho="config/configuration.yaml"):

    absolute_caminho = Path(caminho).resolve()

    with open(absolute_caminho, "r", encoding="utf-8") as f:
        config = yaml.load(f)

    return config
 """   



import yaml
from pathlib import Path

def load_config():
    # Sobe para o diretório raiz do projeto (onde está app.py)
    root = Path(__file__).resolve().parent.parent

    # Caminho completo do config.yaml
    absolute_root = root / "config" / "configuration.yaml"

    with open(absolute_root, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
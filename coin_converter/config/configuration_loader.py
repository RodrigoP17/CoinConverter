
import yaml
from pathlib import Path

def load_config():
    
    root = Path(__file__).resolve().parent.parent

    absolute_root = root / "config" / "configuration.yaml"

    with open(absolute_root, "r", encoding="utf-8") as f:

        return yaml.safe_load(f)

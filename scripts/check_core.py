import importlib.machinery
from pathlib import Path

root = Path(__file__).resolve().parents[1]
core = root / "core"

ok = bool(list(core.glob("app*.so"))) or (core / "app").exists()
if not ok:
    raise SystemExit("未找到匹配 Python 3.10 的 core/app*.so 或 core/app/")
print("core ok")

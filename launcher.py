import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = ROOT / "core"
if str(CORE) not in sys.path:
    sys.path.insert(0, str(CORE))

import app


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--device-id", action="store_true")
    p.add_argument("--config", default=str(ROOT / "config.json"))
    args = p.parse_args()

    if args.device_id:
        print("DEVICE_ID:", app.device_id())
        return

    app.run(args.config)


if __name__ == "__main__":
    main()

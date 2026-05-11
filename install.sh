#!/usr/bin/env bash
set -euo pipefail

conda env create -f environment.yml || conda env update -f environment.yml --prune
conda run -n dexumi_teleop python scripts/check_core.py
echo "安装完成。下一步执行：./get_device_id.sh"

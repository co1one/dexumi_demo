#!/usr/bin/env bash
set -euo pipefail

if [ ! -f license/license.json ]; then
  echo "缺少 license/license.json，请先联系管理员获取 license。" >&2
  exit 1
fi

conda run -n dexumi_teleop python launcher.py --config config.json "$@"

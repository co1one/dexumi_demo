#!/usr/bin/env bash
set -euo pipefail
conda run -n dexumi_teleop python launcher.py --device-id

# DexUMI Teleop Runtime

请使用 Ubuntu + Python 3.10。

## 1. 克隆仓库

```bash
git clone git@github.com:co1one/dexumi_demo.git
cd dexumi_demo
```

## 2. 创建 conda 环境并安装依赖

```bash
conda create -n dexumi_teleop python=3.10 pip -y -c conda-forge

conda run -n dexumi_teleop python -m pip install \
  -i https://pypi.tuna.tsinghua.edu.cn/simple \
  cryptography numpy opencv-python pyserial python-can pyrealsense2
```

检查 core 是否匹配 Python 3.10：

```bash
conda run -n dexumi_teleop python scripts/check_core.py
```

## 3. 检查硬件

```bash
ls /dev/ttyACM0
ip link show can0
```

默认配置：

```text
手套端口：/dev/ttyACM0
灵巧手 CAN：can0
```

如果 `ls /dev/ttyACM0` 报 `Permission denied`，或程序打不开手套串口，执行：

```bash
sudo apt remove brltty -y
sudo usermod -a -G dialout $USER
newgrp dialout
```

然后重新打开一个终端，再检查：

```bash
groups
ls -l /dev/ttyACM0
```

正常情况下，当前用户应属于 `dialout` 组。通常不需要重启电脑；如果重新打开终端后仍不生效，再reboot并重新登录系统。

## 4. 获取本机 DEVICE_ID

```bash
./get_device_id.sh
```

把完整输出发给管理员：

```text
DEVICE_ID: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

联系方式：

```text
chaoyi0027@gmail.com
```

## 5. 放置 license

收到管理员发来的 `license.json` 后，放到：

```text
license/license.json
```


## 6. 运行

```bash
./run.sh
```

可视化窗口中按 `q` 退出。

## 常见问题

### 缺少或无效 license

检查：

```bash
ls -l license/license.json
./get_device_id.sh
```

### 手套串口权限问题

```bash
sudo apt remove brltty -y
sudo usermod -a -G dialout $USER
newgrp dialout
ls -l /dev/ttyACM0
```

### CAN 接口不存在

```bash
ip link show can0
```

如果没有 `can0`，请先连接并配置 CAN 设备。
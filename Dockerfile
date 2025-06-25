# 使用最小化的 OpenJDK 运行时环境
FROM docker.1ms.run/python:3.13-slim
ADD start.sh /app/start.sh
ADD main.py /app/main.py
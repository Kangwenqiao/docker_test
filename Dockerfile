# 设置基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . .

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 定义环境变量
ENV PYTHONUNBUFFERED=1

# 运行爬取脚本
CMD ["python", "crawl_comments.py"]

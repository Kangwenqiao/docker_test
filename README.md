# 豆瓣电影评论爬虫

这个项目是一个简单的 Python 爬虫，用于定期抓取豆瓣电影的用户评论。它使用 `requests` 和 `beautifulsoup4` 库来获取网页内容并解析 HTML。

## 功能描述

- 定期抓取指定豆瓣电影页面的用户评论。
- 将评论内容输出到控制台。
- 每隔两分钟自动重新抓取一次评论，可持续监控评论的更新。

## 开始使用

以下是如何在本地环境中部署和运行这个爬虫项目的步骤。

### 先决条件

你需要在本地安装以下软件：

- Python 3.9 或更高版本
- Docker (如果你选择使用 Docker 容器运行)

### 安装和运行

首先，克隆或下载此项目代码到本地：

```bash
git clone https://github.com/Kangwenqiao/docker_test.git
cd docker_test
```

#### 使用 Python 直接运行

安装依赖：

```
pip install -r requirements.txt
```

运行脚本：

```
python crawl_comments.py
```



#### 使用 Docker 运行

构建 Docker 镜像：

```
docker build -t douban-comment-crawler .
```

运行容器：

```
docker run --name comment-crawler douban-comment-crawler
```

## 项目文件结构

- `crawl_comments.py` - 主爬虫脚本，包含爬虫的核心功能。
- `Dockerfile` - 用于构建 Docker 镜像的配置文件。
- `requirements.txt` - 列出项目的 Python 依赖。

## 贡献

如果你有任何改进建议或功能添加的想法，欢迎提交 pull request 或创建 issue。

## 许可证

该项目采用 MIT 许可证。详情请查阅 `LICENSE` 文件。

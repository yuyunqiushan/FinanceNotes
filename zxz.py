#下载中国地方政府债券信息公开平台专项债附件


# 导入 requests 库和 BeautifulSoup 库
import requests
from bs4 import BeautifulSoup

# 定义网页的 url
url = "https://www.celma.org.cn/fxqgg/54917.jhtml"

# 定义一个请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

# 发送 get 请求，获取网页的源代码
response = requests.get(url, headers=headers)

# 判断响应状态码是否为 200，表示成功
if response.status_code == 200:
    # 用 BeautifulSoup 解析网页的 HTML 结构
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到所有的附件链接，它们都在 div class="content-fj" 下的 a 标签中
    attachments = soup.find("div", class_="content-fj").find_all("a")

    # 遍历附件链接
    for attachment in attachments:
        # 获取附件的 url，它在 a 标签的 href 属性中
        attachment_url = attachment["href"]

        # 获取附件的标题，它在 a 标签的 title 属性中
        attachment_title = attachment["title"]

        # 判断附件的格式是否为 PDF，它在标题的后缀中
        if attachment_title.endswith(".pdf"):
            # 用 requests 库下载附件
            attachment_response = requests.get(attachment_url, headers=headers)

            # 判断响应状态码是否为 200，表示成功
            if attachment_response.status_code == 200:
                # 以二进制模式打开本地文件，以附件的标题作为文件名
                with open(attachment_title, "wb") as f:
                    # 将响应内容写入文件
                    f.write(attachment_response.content)
                # 打印下载成功的信息
                print(f"Downloaded {attachment_url} to {attachment_title}")
            else:
                # 打印下载失败的信息
                print(f"Failed to download {attachment_url}, status code: {attachment_response.status_code}")
else:
    # 打印获取网页失败的信息
    print(f"Failed to get {url}, status code: {response.status_code}")

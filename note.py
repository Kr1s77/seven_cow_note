# ========================================
# name="Note",
# version="0.1.0",
# description="upload files to qiniu",
# author="CriseLYJ",
# author_email="cirselyj163.com",
# url='https://github.com/CriseLYJ'
# ========================================


import os
import re

# 封装七牛云 文件上传工具
import time

# 你的七牛域名
QINIU_URL = "此处填写你的七牛云外链默认域名"


def upload_file(data, file_url):
    """
    文件上传
    :param data: 需要上传的文件数据
    :return: 文件名
    """

    import qiniu
    access_key = "填写你的七牛云aK"  # 秘钥
    secret_key = "此处填写你的七牛云sk"
    bucket_name = "你的七牛云空间名称"  # 空间名称

    q = qiniu.Auth(access_key, secret_key)
    key = file_url  # 设置文件名, 如果设置为None, 会生成随机文件名

    token = q.upload_token(bucket_name)
    ret, info = qiniu.put_data(token, key, data)
    if ret is not None:  # 上传成功, 返回文件名
        file_name = ret.get("key")
        return file_name

    else:  # 上传失败
        raise BaseException(info)


# 上传
def upload_note():
    path = input("请输入文件路径：")

    # 匹配出文件名
    match_obj = re.match("notes/(.*)", path)
    file_url = match_obj.group(1)

    # 读取文件
    with open(path, "rb") as f:
        html_bytes = f.read()

    # 将文件上传到七牛云
    file_name = upload_file(html_bytes, file_url)
    url = QINIU_URL + file_name
    print("*" * 70)
    print("🐍🐍您上传的文件url为：%s" % url)
    print("*" * 70)

    # 输入文件
    add_to_file(url, file_name)


# 将文件名与上传时间输入到requirements.txt文件中
def add_to_file(url, file_name):
    # 获取当前时间，并格式化为字符串
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # 拼接字符串
    info = "file_name-文件名:" + file_name
    time_now = "upload_time-上传时间:" + local_time
    url_str = "🐍🐍URL-链接:" + url
    str = "=" * 100

    # 将文本写入requirements中
    os.system("echo %s >> logs.txt" % info)
    os.system("echo %s >> logs.txt" % time_now)
    os.system("echo %s >> logs.txt" % url_str)
    os.system("echo %s >> logs.txt" % str)


if __name__ == '__main__':
    # 运行程序
    upload_note()

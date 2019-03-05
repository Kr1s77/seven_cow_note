import os


# 向log中写入信息
def write_logs(info, time_now, url_str, strings):
    os.system("echo %s >> logs.txt" % info)
    os.system("echo %s >> logs.txt" % time_now)
    os.system("echo %s >> logs.txt" % url_str)
    os.system("echo %s >> logs.txt" % strings)


def print_msg(url):
    print("*" * 70)
    print("🐍🐍您上传的文件url为：%s" % url)
    print("*" * 70)
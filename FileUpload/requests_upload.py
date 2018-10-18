import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "http://localhost/uploader"

# 不推荐 一次性文件Load到内存
# files= {"file":open("E:\m1\load_qq.py","rb")}
#
# r = requests.post(url ,files = files)d

# print(r.text)


# 推荐，会以二进制方式上传
encoder = MultipartEncoder(
    fields={"desc": " it 's  only a desc",
            'filexx': ('wwwwww.jpg:', open('ww.jpg', 'rb'), 'image/jpeg')}
)  # filexx  对应前端   input type =file 所对应的name ,  tuple 3项 分别为 （以xx名称上传，将要上传的文件 ，文件类型)

r = requests.post(url, data=encoder, headers={'Content-Type': encoder.content_type})

print(r.request.headers)
print(r.text)

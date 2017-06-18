import random

import rabbit
random_key =["http://www.baidu.com","http://www.taobao.com","无怨无悔的爱着你","I feeling i love u","人都是逼出来的"]
random.shuffle(random_key)
print(random_key)

for key in random_key:

    rabbit.sent_message(key)
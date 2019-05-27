#!/usr/bin/python3

"""
Copyright 2018-2019  Firmin.Sun (fmsunyh@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# -----------------------------------------------------
# @Time    : 5/27/2019 2:00 PM
# @Author  : Firmin.Sun (fmsunyh@gmail.com)
# @Software: ZJ_AI
# -----------------------------------------------------
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import hashlib

import lmdb

env_db = lmdb.open("/home/syh/siamrpn_pp/data/VID_2015_RPN++.lmdb")

txn = env_db.begin()

for key, value in txn.cursor():  # 遍历
    # print(key, value)
    print(key)
    break

path = './data/VID_2015_RPN++/ILSVRC2015_train_00000000/000000.00.x_102.15_29.89.jpg'
key = hashlib.md5(path.encode()).digest()
img_buffer = txn.get(key)
print(img_buffer)

env_db.close()


"""
参考：
https://blog.csdn.net/dcrmg/article/details/79144507

"""
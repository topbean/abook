#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
scale = 100
print("-----执行开始-----")
for i in range(scale+1):
    a, b = "**"*i,'..' * (scale-i)
    c = (i/scale)*100
    print('{:^3.0f}%[{}->{}]'.format (c, a, b))
    time.sleep(0.1)
print("-----执行结束-----")
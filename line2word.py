#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 14:55:39 2018

@author: Rorschach
@mail: 188581221@qq.com
"""
import warnings
warnings.filterwarnings('ignore')
from collections import defaultdict
import jieba 

def split(input_path, dict_path, output_path):
    '''
    加载自定义词典并去除停用词，对文本进行分词
    '''
    jieba.enable_parallel(4)
    
    # 设置 stop_word
    stop_word = defaultdict(int)
    with open('/Users/zt/Desktop/project/stop_words/stop_test.txt', 'r') as stop:
        for line in stop.readlines():
            stop_word[line.rstrip("\n")] = 1
    
    # 设置 user_dict
    jieba.load_userdict(dict_path)
    
    # 导入文本
    with open(input_path, 'r') as i:
        text = i.read()
    
    # 分词
    seg_list = list(jieba.cut(text))
    out = ''
    for word in seg_list:
        if stop_word[word] == 0:
            out += word + '  '
    
    # 写入文件
    with open(output_path, 'w') as o:
        o.write(out)
    
    return print('分词成功！')
    
import time
import jieba.analyse
b = time.time()
split('/Users/zt/Desktop/project/test.txt', '/Users/zt/Desktop/project/user_dict/dict_1.txt', '/Users/zt/Desktop/project/cut.txt')
e = time.time()
print(e-b)

test = '上海合作组织成立近17年来，走过了不平凡的发展历程，成为具有广泛影响的综合性区域组织。成员国全面推进各领域合作，在国际和地区事务中积极发挥建设性作用，树立了相互尊重、公平正义、合作共赢的新型国际关系典范。'
result = jieba.analyse.extract_tags(test, 3)
    
        








import os
import re
import pickle
import json
import importlib

from configs import JSON_SAVE_PATH

import argparse
from argparse import ArgumentParser


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __str__(self):
        return f'{self.count:010d}'

ID_COUNTER = Counter()

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs/running.log',
                    filemode='w')

LOGGER = logging.getLogger('ginstruct')

def load_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)

def save_pickle(file_name, data):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.DEFAULT_PROTOCOL)

def preprocess_text(text: str = ''):
    assert isinstance(text, str)
    text = re.sub(r'^\d+\s*', '', text) # 去除开头的数字
    text = text.strip()
    text = re.sub(r'^[.,;?”’:。，]+', '', text)  # 去除开头的标点符号
    text = re.sub(r'\[(\w+)R\]', r'[\1]', text) # [赞R] 替换为 [赞]
    text = re.sub(r'@\S+\s*', '', text) # 删除 @ 之后的信息
    text = text.strip()
    return text

def download_img(url: str, dest_file: str):
    return True
    import wget
    if not os.path.isfile(dest_file):
        download_try = 10
        while download_try > 0:
            try:
                wget.download(url, dest_file)
                download_try = -9
            except:
                download_try -= 1
                continue
        if download_try == 0:
            return False
    return True

def get_class_from_module(module_name, class_name):
    try:
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    except ModuleNotFoundError:
        return None

def make_data_dict(cur_id, cur_conversations):
    return {
        "id": cur_id,
        "conversations": [
            {
                "from": "user" if i % 2 == 0 else "assistant",
                "value": cur_conversations[i]
            } for i in range(len(cur_conversations))
        ]}

def save_results(data, data_id2file_name) -> None:
    with open(os.path.join(JSON_SAVE_PATH, 'data.json'), 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    with open(os.path.join(JSON_SAVE_PATH, 'map.csv'), 'w', encoding='utf-8') as csv_file:
        csv_file.write("data_id,file_name\n")
        for key, value in data_id2file_name.items():
            csv_file.write(f"{key},{value}\n")

def get_command_line_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp', type=str, default='meishichina')
    parser.add_argument('--infer', nargs='*', default=None, required=True)

    args, _ = parser.parse_known_args()
    parser = ArgumentParser(parents=[parser], add_help=False)

    return args, parser

import pprint
_utils_pp = pprint.PrettyPrinter()
def pprint(x):
    _utils_pp.pprint(x)
from pathlib import Path

DATA_PATHS = {
    'meishichina': f'data/meishichina',
    'daydaycook': f'/data/zhangyk/vllm/daydaycook',
    'douguo': f'/data/zhangyk/vllm/douguo',
    'xiachufang': f'/data/zhangyk/vllm/xiachufang',
    'xinshipu': f'/data/zhangyk/vllm/xinshipu',
    'shipuxiu': f'/data/zhangyk/vllm/shipuxiu',
    'meishijie':f'data/meishijie'
}

JSON_SAVE_PATH = 'vllmnd'
IMG_SAVE_PATH = 'vllmnd/imgs'
IMG_DOWNLOAD_FAILED_LOGS = 'vllmnd/img_download_failed.csv'
IMG_DOWNLOAD_TODO = 'vllmnd/imgs.csv'

Path(IMG_SAVE_PATH).mkdir(parents=True, exist_ok=True)


OPEN_AI_KEY = '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' # NOTE: DO NOT UPLOAD

RAW_PROMPT = '''{请基于数据描述和一些示例任务，设计更多任务，并以一个字典返回，包括指令、输入和输出字段，其中示例数据描述和示例任务都是例子。
示例数据描述：
标题：腌糖蒜
描述：腌好的糖蒜鲜而不辣，酸甜可口，最重要的一点是用这种方法腌的糖蒜吃过后嘴里不会有蒜味！去除了你吃蒜后怕口中有大蒜味的后顾之忧。
材料：主料新鲜大蒜5000克、精盐500克、醋500克，辅料水3500克。
步骤：
(1) 准备好新鲜的大蒜。(2) 将鲜蒜去须茎，剥去外皮，放在清水中泡3天（每天换2到3次水，以去掉蒜的异味）。(3) 泡好的蒜捞出，沥干水份。(4) 把蒜放入容器中，一层蒜洒一层盐，每天翻动一次。(5) 腌到第四天的时候把蒜捞出，沥水，晒干。(6) 锅中放3500克水，加入红糖，醋，煮开。(7) 将晒好的蒜放入坛子中，倒入放凉的糖醋水，腌大约一个月左右即可食用了。
技巧：注意要及时端离火口，静置放凉。
示例任务：
{'指令': '请回答菜品的主要材料', '输入': '腌糖蒜', '输出': '主料新鲜大蒜5000克、精盐500克、醋500克'}
{'指令': '请回答制作菜品时的技巧', '输入': '腌糖蒜', '输出': '注意要及时端离火口，静置放凉。'}
{'指令': '请回答蒜要在清水中泡几天', '输入': '腌糖蒜', '输出': '泡三天，每天换两到三次水'}
}
用户问题：根据下面数据描述仿照上述例子生成任务'''
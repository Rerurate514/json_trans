import json
from googletrans import Translator

# 翻訳器のインスタンスを作成
translator = Translator()

import re

def validate_input(input_string):
    pattern = r'^[0-9a-zA-Z\s\%\$\s]+$'
    match = re.match(pattern, input_string)
    
    if match is None:
        return False  # 変換処理を終了

    # 入力が有効な場合の処理
    return True  # 正常終了

def translate_text(text):
    if type(text) is not str or type(text) is None or not validate_input(text):
        return text

    try:
        translated = translator.translate(text, src='en', dest='ja')
        return translated.text
    except:
        return text

    return text

def translate_json_keys(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    translated_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            translated_data[key] = translate_json_keys(value)
        elif isinstance(value, str):
            translated_value = translate_text(value)  # 値を翻訳
            translated_data[key] = translated_value
            print(translated_data[key])
        else:
            translated_data[key] = value
    
    return translated_data

# JSONファイルのパスを指定
file_path = 'en.json'
translated_data = translate_json_keys(file_path)

# 翻訳後のデータをJSON形式で出力
with open('ja_jp.json', 'w', encoding='utf-8') as file:
    json.dump(translated_data, file, ensure_ascii=False, indent=4)
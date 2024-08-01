import json
from translate import Translator

def translate_text(text):
    translator = Translator(from_lang = "en", to_lang = "ja")
    result = translator.translate(text)
    return result

def translate_json_keys(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    translated_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            translated_data[key] = translate_json_keys(value)
        elif isinstance(value, str):
            translated_key = f"{value}"  # 新しいキー名を生成
            translated_value = translate_text(value)  # 値を翻訳
            translated_data[translated_key] = translated_value
        else:
            translated_data[key] = value
        print(translated_data)
    
    return translated_data

# JSONファイルのパスを指定
file_path = 'en.json'
translated_data = translate_json_keys(file_path)

# 翻訳後のデータをJSON形式で出力
with open('ja_jp.json', 'w', encoding='utf-8') as file:
    json.dump(translated_data, file, ensure_ascii=False, indent=4)

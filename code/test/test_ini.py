import configparser
import os

# 创建ConfigParser对象
config = configparser.ConfigParser()
env = os.environ.get('APP_ENV','dev')
current_path = os.getcwd()
parent_path = os.path.dirname(current_path)
grandparent_path = os.path.dirname(parent_path)

print("Current Path:", current_path)
print("Parent Path:", parent_path)
print("Grandparent Path:", grandparent_path)
config.read(f'config/{env}.ini')
print(f'config/{env}.ini')
# config.read(f'D:\Desktop\workRelated\chatgpt\pythonProject1\config\dev.ini')

# 获取DEFAULT部分的OUTPUT_DIR值
print(config.sections())
# output_dir = config['DEFAULT']['OUTPUT_DIR']

# 打印输出
# print(output_dir)
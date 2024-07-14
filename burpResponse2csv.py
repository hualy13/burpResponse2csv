import json
import csv

# 读取txt文件内容
with open('response.txt', 'r', encoding='utf-8') as file:  # 打开名为'response.txt'的文本文件，以读取模式，并指定编码为'utf-8'
    lines = file.readlines()  # 读取文件的所有行，并将其存储在'lines'列表中

# 查找并提取JSON内容
json_data = None  # 初始化json_data变量为None
for line in lines:  # 遍历'lines'中的每一行
    if line.strip().startswith('{') and line.strip().endswith('}'):  # 检查行是否以'{'开始并以'}'结束
        json_data = line.strip()  # 如果是，则将该行去除首尾空格后赋值给json_data
        break  # 找到后跳出循环

# 检查是否成功提取到JSON数据
if json_data:  # 如果json_data不是None
    data = json.loads(json_data)  # 将json_data解析为Python字典并存储在'data'中
else:
    raise ValueError("未找到有效的JSON数据")  # 否则抛出错误，提示未找到有效的JSON数据

# 提取需要的字段
rows = data['data']['rows']  # 从解析后的数据中提取'response.txt'内的记录行
fieldnames = set()  # 初始化字段名集合

# 通过遍历所有记录来动态更新字段名列表
for row in rows:  # 遍历每一行记录
    fieldnames.update(row.keys())  # 更新字段名集合，以包含所有字段名

# 写入到CSV文件
csv_filename = 'output.csv'  # 指定输出的CSV文件名
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:  # 打开名为'output.csv'的文件，以写入模式，并指定编码为'utf-8'
    csv_writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))  # 创建一个DictWriter对象，用于将字典写入到CSV文件
    csv_writer.writeheader()  # 写入CSV文件头（字段名）
    csv_writer.writerows(rows)  # 将记录行写入到CSV文件

print(f"数据已成功写入到 {csv_filename}")  # 打印成功消息，指示数据已成功写入到指定的CSV文件中

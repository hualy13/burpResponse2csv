import json
import csv

# 读取 txt 文件内容
with open('response.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 查找并提取 JSON 内容
json_data = None
for line in lines:
    if line.strip().startswith('{') and line.strip().endswith('}'):
        json_data = line.strip()
        break

# 检查是否成功提取到 JSON 数据
if json_data:
    data = json.loads(json_data)
else:
    raise ValueError("未找到有效的 JSON 数据")

# 提取需要的字段
rows = data['data']['rows']
fieldnames = set()

# 通过遍历所有记录来动态更新字段名列表
for row in rows:
    fieldnames.update(row.keys())

# 写入到 CSV 文件
csv_filename = 'output.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:  # 使用 'utf-8-sig' 编码
    csv_writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))
    csv_writer.writeheader()
    csv_writer.writerows(rows)

print(f"数据已成功写入到 {csv_filename}")

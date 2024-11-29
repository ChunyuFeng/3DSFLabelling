# 此脚本用于读取 nuscenes/samples/LIDAR_TOP/ 以及 nuscenes/sweeps/LIDAR_TOP/ 目录下的数据
# 并将其文件名按照时间戳的顺序，保存到 lidar_lut.txt 中

import os
import re

samples_path = './dataset/nuscenes/samples/LIDAR_TOP/'
sweeps_path = './dataset/nuscenes/sweeps/LIDAR_TOP/'

sample_names = os.listdir(samples_path)
# 合并路径，将 samples/LIDAR_TOP/ 的路径添加到文件名前
sample_names = [os.path.join('samples/LIDAR_TOP/', name) for name in sample_names]

sweep_names = os.listdir(sweeps_path)
# 合并路径，将 sweeps/LIDAR_TOP/ 的路径添加到文件名前
sweep_names = [os.path.join('sweeps/LIDAR_TOP/', name) for name in sweep_names]

# 将 sample_names 和 sweep_names 合并后，按照时间戳排序
lidar_top_names = sample_names + sweep_names

# 提取时间戳的正则表达式
timestamp_pattern = r'__LIDAR_TOP__(\d+)\.pcd\.bin'

# 对文件名按照时间戳进行排序
lidar_top_names_sorted = sorted(
    lidar_top_names,
    key=lambda x: int(re.search(timestamp_pattern, x).group(1))  # 提取并转换为整数进行排序
)

# 将文件名写入txt文件
with open('./dataset/nuscenes/lidar_top_names_sorted.txt', 'w') as f:
    for file_name in lidar_top_names_sorted:
        f.write(file_name + '\n')

# 将文件名的前100个写入txt文件
with open('./dataset/nuscenes/lidar_top_names_sorted_100.txt', 'w') as f:
    for file_name in lidar_top_names_sorted[:100]:
        f.write(file_name + '\n')

print("文件名已写入 'lidar_top_names_sorted.txt'")

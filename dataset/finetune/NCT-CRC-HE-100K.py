import os
import shutil
import random


def split_dataset(source, train_ratio=0.8, val_ratio=0.1):
    # 获取所有.jpg文件
    all_files = [f for f in os.listdir(source) if f.endswith('.tif')]
    random.shuffle(all_files)

    # 计算每个集合的大小
    total_files = len(all_files)
    train_size = int(total_files * train_ratio)
    val_size = int(total_files * val_ratio)

    # 保存各部分文件名
    train, val, test = [], [], []
    for i, file in enumerate(all_files):
        if i < train_size:
            train.append(os.path.join(source, file))
        elif i < train_size + val_size:
            val.append(os.path.join(source, file))
        else:
            test.append(os.path.join(source, file))
    return train, val, test


if __name__ == "__main__":
    origin_prefix = 'original/NCT-CRC-HE-100K/'
    target_prefix = 'nct/'

    total_train, total_val, total_test = [], [], []
    origin_path = origin_prefix
    for p in os.listdir(origin_path):
        train, val, test = split_dataset(os.path.join(origin_path, p), train_ratio=0.8, val_ratio=0.1)
        total_train.extend(train)
        total_val.extend(val)
        total_test.extend(test)

    train_folder = os.path.join(target_prefix, 'train')
    val_folder = os.path.join(target_prefix, 'val')
    test_folder = os.path.join(target_prefix, 'test')

    for f in total_train:
        file_name = f.split('/')[-1]
        class_type = file_name.split('-')[0]
        if not os.path.exists(os.path.join(train_folder, class_type)):
            os.makedirs(os.path.join(train_folder, class_type))
        shutil.copy(f, os.path.join(train_folder, class_type, file_name))
    for f in total_val:
        file_name = f.split('/')[-1]
        class_type = file_name.split('-')[0]
        if not os.path.exists(os.path.join(val_folder, class_type)):
            os.makedirs(os.path.join(val_folder, class_type))
        shutil.copy(f, os.path.join(val_folder, class_type, file_name))
    for f in total_test:
        file_name = f.split('/')[-1]
        class_type = file_name.split('-')[0]
        if not os.path.exists(os.path.join(test_folder, class_type)):
            os.makedirs(os.path.join(test_folder, class_type))
        shutil.copy(f, os.path.join(test_folder, class_type, file_name))


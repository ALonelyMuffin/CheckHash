import hashlib
import os
import time
# import pprint
import json
# import cProfile

# os.path.getsize(file)
start_time = time.time()


'''
Files = {
    hash_1 = [path_1, path_2, ...],
    "f78fb" = [dolphin.mp4, dolphin_2.mp4]
    "0963e" = [dolphin_3.mp4]
}
'''
# dir_1 = r"D:\Backup 2017\Video"
# dir_2 = r"C:\Users\Richie\Downloads\backup\Video"

dir_1 = r"C:\Users\Richie\Downloads\Back\screenshots"
dir_2 = r"C:\Users\Richie\Pictures\MinecraftScreenshots"

files_1 = [f for f in os.listdir(dir_1) if os.path.isfile(os.path.join(dir_1, f))]
files_2 = [f for f in os.listdir(dir_2) if os.path.isfile(os.path.join(dir_2, f))]

hash_1 = []
hash_2 = []


hash_data = {
    "a" : "test"
}

def hashFiles(main_dir):
    for root, subdirs, files in os.walk(main_dir):
        for f in files:
            file_path = os.path.join(root, f)
            
            with open(file_path, 'rb') as f:

                data = f.read()
                hash_info = hashlib.md5(data).hexdigest()

                if hash_info in hash_data:
                    hash_data[hash_info].append(file_path)
                else:
                    hash_data[hash_info] = [file_path]


def getHashFiles(dirs, files):
    tmp = []
    for i in files:

        with open(os.path.join(dirs, i), 'rb') as f:

            data = f.read()
            hash_info = hashlib.md5(data).hexdigest()

            if hash_info in hash_data:
                hash_data[hash_info].append(os.path.join(dirs, i))
            else:
                hash_data[hash_info] = [os.path.join(dirs, i)]

            tmp.append(hash_info)
    return tmp

# hash_1 = getHashFiles(dir_1, files_1)
# hash_2 = getHashFiles(dir_2, files_2)

# for i in range(len(hash_1)):
#     if (hash_1[i] == hash_2[i]):
#         print(f"{hash_1[i][26:]} == {hash_2[i][26:]}")
#     else:
#         print(f"{hash_1[i][26:]} || {hash_2[i][26:]}")

hashFiles(dir_1)
hashFiles(dir_2)

with open(r'C:\Users\Richie\Desktop\test.json', 'w') as f:
    f.write(json.dumps(hash_data, indent=4))

# print(hash_1[26:])


end_time = time.time()
print("{:.6f}s".format(end_time - start_time))
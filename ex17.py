from sys import argv
from os.path import exists

scirpt, ori_flie, dup_file = argv

print(f"To {ori_flie} From {dup_file}")

#
ip_file = open(ori_flie, encoding='utf-8')
in_data = ip_file.read()

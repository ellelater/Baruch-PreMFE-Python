
import os
import shutil

# a. Create a new directory.
newpath = r'/Users/zhipengyan/Desktop/Python'
if not os.path.exists(newpath):
    os.mkdir(newpath)

# b. Rename the above directory.
os.rename('/Users/zhipengyan/Desktop/Python', '/Users/zhipengyan/Desktop/Pycharm')

# c. Delete the above directory.
os.removedirs('/Users/zhipengyan/Desktop/Pycharm')

# d. Create another directory and create two text files in this directory.
os.mkdir('/Users/zhipengyan/Desktop/Python')
open('/Users/zhipengyan/Desktop/Python/1.xlsx', 'a').close()
open('/Users/zhipengyan/Desktop/Python/2.xlsx', 'a').close()

# e. Delete one of the text files from the above directory.
try:
    os.remove('/Users/zhipengyan/Desktop/Python/1.xlsx')
except OSError:
    pass

# f. Rename the remaining text file.
os.rename('/Users/zhipengyan/Desktop/Python/2.xlsx', '/Users/zhipengyan/Desktop/Python/stock_price.xlsx')

# g. Create a subdirectory within the above created directory.
os.makedirs('/Users/zhipengyan/Desktop/Python/level1')

# h. Move the remaining text file into the subdirectory.
shutil.rmtree('/Users/zhipengyan/Desktop/Python')
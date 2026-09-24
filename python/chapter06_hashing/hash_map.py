import sys
from pathlib import Path

if __name__ == "__main__":
    #初始化哈希表
    hamp = dict[int, str]()
    
    #添加键值对
    hamp[12444] = "小哈"
    
    #查询操作
    name : str = hamp[12444]
    
    #删除操作
    hamp.pop(12444)
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from chapter_hashing.array_hash_map import Pair

class HashMapOpenAddressing:
    """开放寻址哈希表"""
    def __init__(self):
        """构造方法"""
        # 键值对数量
        self.size = 0
        #哈希表数量
        self.capacity = 4
        # 触发扩容的负载因子阈值
        self.load_thres = 2.0 / 3.0
        # 扩容倍数
        self.extend_ratio = 2
        # 桶数组
        self.buckets: list[Pair|None] = [None]*self.capacity
        # 删除标记
        self.TOMBSTONE = Pair(-1,'-1')
    
    def hash_func(self, key: int) -> int:
        """哈希函数"""
        return key % self.capacity
        
    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity
        
    def find_bucket(self, key: int) -> int:
        """搜索 key 对应的桶索引"""
        index = self.hash_func(key)
        first_tombstone = -1
        # 线性探测，遇到空桶退出循环
        while self.buckets[index] is not None:
            if self.buckets[index].key == key:
                #在之前就遇到TOMBSTONE了,交换两个
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone
                return index
            # 记录遇到首个TOMBSTONE
            if first_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tombstone = index
            index = (index+1)% self.capacity
        # 若桶为空，就返回这个桶的坐标，方便写入
        return index if first_tombstone == -1 else first_tombstone
            
        
    def get(self, key: int) -> str|None:
        """查询操作"""
        index = self.find_bucket(key)
        
        if self.buckets[index] not in [None,self.TOMBSTONE]:
            return self.buckets[index].val
        return None
    
    def put(self, key: int, val: str):
        """添加操作"""
        ## 记得检查负载因子
        if self.load_factor() > self.load_thres:
            self.extend()
            
        index = self.find_bucket(key)
        
        if self.buckets[index] not in [None,self.TOMBSTONE]:
            self.buckets[index].val = val
        else:
            pair = Pair(key,val)
            self.buckets[index] = pair
            self.size+=1
        
    def remove(self, key: int):
        """删除操作"""
        index = self.find_bucket(key)
        if self.buckets[index] not in [None,self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -=1
    
    def extend(self):
        """扩容哈希表"""
        buckets_tmp = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        for pair in buckets_tmp:
            if pair not in [None,self.TOMBSTONE]:
                self.put(pair.key,pair.val)
        
    def print(self):
        """打印哈希表"""
        for pair in self.buckets:
            if pair is None:
                print('None')
            elif pair is self.TOMBSTONE:
                print('TOMBSTONE')
            else :
                print(pair.key,"->",pair.val)
    
    """Driver Code"""
if __name__ == "__main__":
    # 初始化哈希表
    hashmap = HashMapOpenAddressing()

    # 添加操作
    # 在哈希表中添加键值对 (key, val)
    hashmap.put(12836, "小哈")
    hashmap.put(15937, "小啰")
    hashmap.put(16750, "小算")
    hashmap.put(13276, "小法")
    hashmap.put(10583, "小鸭")
    print("\n添加完成后，哈希表为\nKey -> Value")
    hashmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 val
    name = hashmap.get(13276)
    print("\n输入学号 13276 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, val)
    hashmap.remove(16750)
    print("\n删除 16750 后，哈希表为\nKey -> Value")
    hashmap.print()
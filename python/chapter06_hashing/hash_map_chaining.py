import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from chapter_hashing.array_hash_map import Pair

class HashMapChaining:
    """链式地址哈希表"""
    
    def __init__(self):
        """构造方法"""
        # 键值对数量
        self.size = 0
        # 哈希表容量
        self.capacity = 4
        # 触发扩容的负载因子阈值
        self.load_thres = 2.0/3.0
        # 扩容倍数
        self.extend_ratio = 2
        # 桶数组
        self.buckets = [[] for _ in range(self.capacity)]
    
    def hash_func(self, key: int) -> int:
        """哈希函数"""
        index = key % self.capacity
        return index
        
    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity
    
    def get(self, key: int) -> str | None:
        """查询操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return None
        
    def put(self, key : int, val: str):
        """添加操作"""
        if self.load_factor() > self.load_thres: #忘记判断阈值是否越界
            self.extend()
        
        index = self.hash_func(key)
        bucket = self.buckets[index]  #这两个指向同一个对象，改变bucket里的值，buckets里的相应对象也会改变
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        pair = Pair(key,val)
        bucket.append(pair)
        self.size += 1  #忘记增加
        
        
            
    # def put(self, key: int, val: str):
    #     """添加操作"""
    #     index = self.hash_func(key)
    #     bucket = self.buckets[index]
    #     pair : Pair = Pair(key,val)
        
                 
    
    def remove(self, key: int):
        """删除操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # bucket.remove(),不能直接这样写
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break
        
        
    def extend(self):
        """扩容哈希表"""
        # 需要暂存哈希表
        buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size =0
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key,pair.val)
                
    def print(self):
        """打印哈希表"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + '->'+ pair.val)
                print(res)
    
    """Driver Code"""
if __name__ == "__main__":
    # 初始化哈希表
    hashmap = HashMapChaining()

    # 添加操作
    # 在哈希表中添加键值对 (key, value)
    hashmap.put(12836, "小哈")
    hashmap.put(15937, "小啰")
    hashmap.put(16750, "小算")
    hashmap.put(13276, "小法")
    hashmap.put(10583, "小鸭")
    print("\n添加完成后，哈希表为\n[Key1 -> Value1, Key2 -> Value2, ...]")
    hashmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 value
    name = hashmap.get(13276)
    print("\n输入学号 13276 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, value)
    hashmap.remove(12836)
    print("\n删除 12836 后，哈希表为\n[Key1 -> Value1, Key2 -> Value2, ...]")
    hashmap.print()
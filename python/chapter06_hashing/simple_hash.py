def add_hash(key:str)-> str:
    """加法哈希"""
    hash = 0
    modulus =  1000000007
    for c in key:
        hash += ord(c)
    return hash % modulus

def mul_hash(key:str) -> int:
    """乘法哈希"""
    hash = 0
    modulus =  1000000007
    for c in key:
        hash = 31 * hash + ord(c)
    return hash % modulus

def xor_hash(key:str)->int:
    """异或哈希"""
    hash = 0
    modulus =  1000000007
    for c in key:
        hash ^= ord(c)
    return hash % modulus
    
def rot_hash(key:str)-> int:
    """循环哈希"""
    hash = 0
    modulus =  1000000007
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % modulus
    
    
if __name__ == '__main__':
    key = 'wjz2005'
    key1 = '2005wjz'
    
    hash1 = add_hash(key)
    hash2 = add_hash(key1)
    print(f'加法哈希1为：{hash1}')
    print(f'加法哈希2为：{hash2}')
    
    hash = mul_hash(key)
    hash1 = mul_hash(key1)
    print(f'乘法哈希1为：{hash}')
    print(f'乘法哈希2为：{hash1}')

    hash = xor_hash(key)
    hash1 = xor_hash(key1)
    print(f'异或哈希1为：{hash}')
    print(f'异或哈希2为：{hash1}')    
    
    hash = rot_hash(key)
    hash1 = rot_hash(key1)
    print(f'循环哈希1为：{hash}')
    print(f'循环哈希2为：{hash1}')
# 线性代数

## 向量
有向线段，从原点开始
#### 向量的基础运算

1. 向量取模(向量的长度)：
![image](https://raw.githubusercontent.com/xxg3053/learn-pyspark/master/linear_algebra/img/vector_qm.png)
```python
def norm(self):
    """返回向量的模"""
    return math.sqrt(sum(e**2 for e in self._values))
```
 
2. 向量加法
```python
def __add__(self, other):
    """向量加法，返回结果向量"""
    assert len(self) == len(other),\
        "Error in adding. Length of vectors must be same."
    return Vector([a + b for a,b in zip(self, other)])
```
3. 向量乘法(标量与向量相乘)
```python
def __mul__(self, other):
    """向量乘法，返回结果向量： self * other"""
    return Vector([other * e for e in self])

def __rmul__(self, other):
    """向量乘法，返回结果向量： other * self"""
    return self * other
```

#### 向量的长度和单位向量

单位向量   

||u||= 1 只表示方向   
vector_qm.png

#### 向量的点乘
向量乘以向量
   

三角函数：  
![image](https://raw.githubusercontent.com/xxg3053/learn-pyspark/master/linear_algebra/img/triangle_func.png)

向量的点乘： 
```python
def dot(self, other):
        """向量的点乘，返回结果标量"""
        assert len(self) == len(other),\
            "Error in dot product. Length of vectors must be same."
        return sum(a * b for a,b in zip(self, other))
    
```

###### 向量点乘的应用
1. 看两个向量的夹角
- v*u=0,两个向量垂直
- v*u>0,两个向量夹角为锐角
- v*u<0,两个向量夹角为钝角 

2. 判断两个向量的相似程度（推荐系统） 
- 锐角：相似     
- 垂直：无关   
- 钝角：不相似  

3. 投影点的坐标

#### numpy中向量的使用
[代码](https://github.com/xxg3053/learn-pyspark/blob/master/linear_algebra/main_numpy_vector.py)


#利用reduce函数设计求list中元素的积
#By using the reduce function to obtain the product of a list
input = [1, 2 ,4 ,12, 5]

def prod(m, n):
    return m*n

mul = reduce(prod, input)
print mul

import numpy as np





#bulim = np.linspace(0.1,1,20)
#tulim = np.linspace(0.1,1,20)
#blim = np.linspace(0.1,1,20)
np.save('tmp123', np.array([[1, 2, 3], [4, 5, 6]]))
np.load('tmp123.npy')
#kl = np.load('tmp123.npy')
print("np.load('tmp123.npy')",np.load('tmp123.npy'))
'''
array([[1, 2, 3],
       [4, 5, 6]])
Store compressed data to disk, and load it again:
'''
a = np.array([[1, 2, 3], [4, 5, 6]])
b=np.array([1, 2])
print("a",a)
print("b",b)
np.savez('tmp.npz', a=a, b=b)

data = np.load('tmp.npz')
data['a']
print("data['a']",data['a'])
print("data['b']",data['b'])
'''
array([[1, 2, 3],
       [4, 5, 6]])
'''
data['b']
'''

array([1, 2])
'''
data.close()
#Mem-map the stored array, and then access the second row directly from disk:
X = np.load('tmp123.npy', mmap_mode='r')
'''
 X[1, :]
memmap([4, 5, 6])
'''

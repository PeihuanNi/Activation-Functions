import numpy as np
import matplotlib.pyplot as plt

# 定义 Sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 定义 Swish 函数
def swish(x):
    return x * sigmoid(x)

# 生成 x 值
x = np.linspace(-5, 5, 400)

# 计算 y 值
y = swish(x)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Swish', color='green')
plt.title('Swish Activation Function')
plt.xlabel('x')
plt.ylabel('Swish(x)')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()

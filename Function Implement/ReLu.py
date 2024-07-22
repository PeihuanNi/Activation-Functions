import numpy as np
import matplotlib.pyplot as plt

# 定义 ReLU 激活函数
def relu(x):
    return np.maximum(0, x)

# 生成 x 值
x = np.linspace(-5, 5, 400)

# 计算 y 值
y = relu(x)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='ReLU', color='blue')
plt.title('ReLU Activation Function')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()

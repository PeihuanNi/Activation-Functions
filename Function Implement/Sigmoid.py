import numpy as np
import matplotlib.pyplot as plt

# 定义 Sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 生成 x 值
x = np.linspace(-10, 10, 400)

# 计算 y 值
y = sigmoid(x)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Sigmoid', color='blue')
plt.title('Sigmoid Activation Function')
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

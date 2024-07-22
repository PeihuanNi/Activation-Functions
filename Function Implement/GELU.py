import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

# 定义 GELU 激活函数
def gelu_exact(x):
    return x * 0.5 * (1 + erf(x / np.sqrt(2)))

def gelu_approx(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

# 生成 x 值
x = np.linspace(-5, 5, 400)

# 计算 y 值
y_exact = gelu_exact(x)
y_approx = gelu_approx(x)

# 创建图像
plt.figure(figsize=(12, 8))

plt.plot(x, y_exact, label='GELU (Exact)', color='blue')
plt.plot(x, y_approx, label='GELU (Approx)', color='red', linestyle='--')
plt.title('GELU Activation Function')
plt.xlabel('x')
plt.ylabel('GELU(x)')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()

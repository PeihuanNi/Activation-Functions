# Activation-Function
- ## Sigmoid
  $$\sigma(x)=\frac{1}{1+e^{-x}}$$
  图像为：
  ![image](./Function%20Image/Sigmoid.png)
- ## ReLU
    $$
    ReLU(x)=\begin{cases}
    x, & x\geq0\\
    0, & x<0
    \end{cases}
    $$
    其图像为：
    ![image](./Function%20Image/ReLU.png)
- ## GELU
    GELU在论文 *AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE* 中使用
    $$GELU(x)=x \cdot \Phi(x)$$  

    正态分布的累积分布函数(CDF) $\Phi(x)$ 可以用如下的 LaTeX 公式来表示：

    $$\Phi(x) = \frac{1}{2} \left( 1 + {erf} \left( \frac{x}{\sqrt{2}} \right) \right)$$

    其中，${erf}(x)$ 是误差函数（error function），其定义为：

    $${erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} \, dt$$

    GELU可以近似表示成

    $$GELU(x)=0.5x(1+tanh(\sqrt{\frac{2}{\pi}}(x+0.044715x^3)))$$
    其图像为：
    ![image](./Function%20Image/GELU.png)
- ## Swish
    $$Swish(x)=x\cdot\sigma(x)$$
    其中$\sigma(x)$是Sigmoid函数
    图像为：
    ![image](./Function%20Image/Swish.png)
Swish和GELU都很好的处理了0附近的变化情况，但**Swish函数的计算以及导数相对简单**，即使是使用GELU的简化版本，Swish仍简单一些
# Activation-Function
- ## ReLU
$$
ReLU(x)=\begin{cases}
x, & x\geq0\\
0, & x<0
\end{cases}
$$
- ## GELU
$$GELU(x)=x \cdot \Phi(x)$$  

正态分布的累积分布函数(CDF) $\Phi(x)$ 可以用如下的 LaTeX 公式来表示：

$$\Phi(x) = \frac{1}{2} \left( 1 + {erf} \left( \frac{x}{\sqrt{2}} \right) \right)$$

其中，$$\({erf}(x)\)$$ 是误差函数（error function），其定义为：

$${erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} \, dt$$
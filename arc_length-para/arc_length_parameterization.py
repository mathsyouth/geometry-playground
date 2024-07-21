import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = ['Microsoft YaHei']

# 椭圆的长半轴和短半轴
a = 5
b = 3

# 角度范围
theta = np.linspace(0, 2*np.pi, 1000)

# 弧长微分
ds = np.sqrt(a**2 * np.sin(theta)**2 + b**2 * np.cos(theta)**2)

# 计算弧长 s(theta)
s = cumulative_trapezoid(ds, theta, initial=0)

# 构建弧长 s 和角度 theta 之间的插值函数
# theta_of_s = CubicSpline(s, theta)

# 定义弧长参数化的 s 范围
s_values = np.linspace(0, s[-1], 1000)

# 计算弧长参数化的 x(s) 和 y(s)
# theta_values = theta_of_s(s_values)
theta_values = np.interp(s_values, s, theta)
x_values = a * np.cos(theta_values)
y_values = b * np.sin(theta_values)

# 绘制椭圆及其弧长参数化
plt.plot(x_values, y_values, label='椭圆')
plt.xlabel('x')
plt.ylabel('y')
plt.title('椭圆的弧长参数化')
plt.legend()
plt.axis('equal')
plt.show()

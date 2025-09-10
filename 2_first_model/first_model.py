import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

print("first model")

# 生成线性数据
np.random.seed(55) # 为了可重复性设置随机种子

x_data = np.linspace(-1, 1, 100)
print(x_data)

y_data = 2 * x_data + 1 + np.random.randn(100) * 0.33  # 生成 y 数据，y = 2x + 1，加上一些噪声
print(y_data)

# 一个输入层和一个输出层
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# 为优化器: 梯度下降（SGD）
# 损失函数: 均方误差（MSE）
model.compile(optimizer='sgd', loss='mse')

# 训练模型
model.fit(x_data, y_data, epochs=50)

# 评估模型
loss = model.evaluate(x_data, y_data)
print(f"Mean Squared Error: {loss}")

# 使用模型进行预测
predictions = model.predict(x_data)
print("Predictions:", predictions)


# plt.scatter(x_data, y_data, color='blue', label='Actual data')  # 绘制实际数据点
# plt.plot(x_data, predictions, color='red', label='Fitted line')  # 绘制拟合线
# plt.legend()
# plt.show()


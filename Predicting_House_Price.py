import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
plt.style.use('dark_background')
x_train=np.array([1.0,2.0])
y_train=np.array([300,500])
m=len(x_train)
w=200
b=100
def calculate_model_output(w,b,x):
    m=x.shape
    f_wb=np.zeros(m)
    for i in range (len(x)):
        f_wb[i]=w*x[i]+b
    return f_wb
temp_f_wb=calculate_model_output(w,b,x_train)
plt.plot(x_train,temp_f_wb,c='b',label="Our Predictions")
plt.scatter(x_train,y_train,marker='x',c='r',label="Actual values")
plt.title("Housing Price")
plt.ylabel("Price(in 1000 dollars)")
plt.xlabel("size(in 1000 Square feet)")
plt.legend()
plt.show()
cost_predict= w*1.200+b
print(cost_predict)
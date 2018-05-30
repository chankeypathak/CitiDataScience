import matplotlib.pyplot as plt

y_1 = [0.,0.2,0.4,0.6,0.8,1.,
       1.2,1.4,1.6,1.8,2.,
       2.2,2.4,2.6,2.8,3.,
       3.2,3.4,3.6,3.8,4.,
       4.2,4.4,4.6,4.8,5.]
y_2 = [v**2 for v in y_1]
y_3 = [v**3 for v in y_1]
plt.plot(y_1, y_1, 'r--', y_1, y_2, 'bs', y_1, y_3, 'g^') 
plt.show()

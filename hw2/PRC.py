import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
plt.figure(1)
plt.title('Precision/Recall Curve')# give plot a title
plt.xlabel('Recall')# make axis labels
plt.ylabel('Precision')
 

recall = np.array([1/7, 2/7, 2/7, 3/7, 4/7, 5/7, 5/7, 6/7, 6/7, 1])
precision = np.array([1, 1, 2/3, 3/4, 4/5, 5/6, 5/7, 3/4, 2/3, 0.7])
print(precision, recall)
plt.figure(1)
plt.plot(recall, precision)
plt.show()
plt.savefig('p-r.png')
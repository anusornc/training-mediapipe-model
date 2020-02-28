import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0.475879, 0.733531],
                 [0.386431, 0.71439],
                 [0.323298, 0.619838],
                 [0.283907, 0.512518],
                 [0.237722, 0.426644],
                 [0.386384, 0.417599],
                 [0.357963, 0.303085],
                 [0.341708, 0.216809],
                 [0.329537, 0.138992],
                 [0.450951, 0.401847],
                 [0.449954, 0.254865],
                 [0.444587, 0.164428],
                 [0.436292, 0.0975653],
                 [0.504699, 0.422285],
                 [0.510112, 0.298018],
                 [0.497089, 0.361776],
                 [0.485562, 0.428335],
                 [0.559963, 0.47175],
                 [0.567432, 0.376727],
                 [0.552384, 0.397112],
                 [0.536558, 0.430559]])

x, y = data.T
plt.scatter(x, y)
plt.show()
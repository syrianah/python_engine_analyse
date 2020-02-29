

from scipy.interpolate import interp1d
import numpy as np
import csv
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


input_path = "test-29-02-2020/ScaledData.csv"
output_path = "test-29-02-2020/thrust_2.png"

thrust = []
time = []

with open(input_path) as f:
    data = csv.reader(f)
    for sample in data:
        thrust.append(float(sample[2]) * 10)
        time.append(int(sample[0]))

print(thrust)
print(time)


f2 = interp1d(time, thrust)
xnew = np.linspace(0, 140, num=40, endpoint=True)


fig, ax = plt.subplots()
ax.plot(xnew, f2(xnew), label='three grains', color='red')


ax.set(xlabel='time (ms)', ylabel='thrust (N)',
       title='Chart of the thrust to time')
ax.grid()

plt.legend(frameon=True, loc='upper right', ncol=2)

fig.savefig(output_path)
plt.show()

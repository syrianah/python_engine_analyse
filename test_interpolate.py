import numpy as np
import json
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

input_path = "pomiary/read.json"
output_path = "obliczenia/test-read.png"


def prepare_to_plot(data_path):
    with open(data_path) as f:
        file = json.load(f)

    thrust_array = []
    time_array = []

    for sample in file:
        # thrust_array.append(sample["temp"])
        thrust_array.append(sample["thrust"]*10)
        time_array.append(sample["time"])
        # print(sample["thrust"])

    new_time_array = []
    for i in range(len(time_array)):
        try:
            if i == 0:
                new_time_array.append(0)
                time_diff = time_array[i+1] - time_array[i]
                time = new_time_array[i] + time_diff
                new_time_array.append(time)
            else:
                time_diff = time_array[i+1] - time_array[i]
                time = new_time_array[i] + time_diff
                new_time_array.append(time)
        except:
            pass

    print(thrust_array)
    print(new_time_array)
    return new_time_array, thrust_array

# Multi plot

# with open('pomiary/READOUTS_KAL_45.json') as f:
#     file = json.load(f)

# thrust_array = []
# time_array = []

# for sample in file:
#     thrust_array.append(sample["thrust"]*10)
#     time_array.append(sample["time"])
#     # print(sample["thrust"])

# new_time_array = []
# for i in range(len(time_array)):
#     try:
#         if i == 0:
#             new_time_array.append(0)
#             time_diff = time_array[i+1] - time_array[i]
#             time = new_time_array[i] + time_diff
#             new_time_array.append(time)
#         else:
#             time_diff = time_array[i+1] - time_array[i]
#             time = new_time_array[i] + time_diff
#             new_time_array.append(time)
#     except:
#         pass

# print(file)
# print(thrust_array)
# print(new_time_array)

# Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

# time45, thrust45 = prepare_to_plot('pomiary/READOUTS_KAL_45.json')
# time50, thrust50 = prepare_to_plot('pomiary/READOUTS_KAL_50.json')
# time55, thrust55 = prepare_to_plot('pomiary/READOUTS_KAL_55.json')
# time60, thrust60 = prepare_to_plot('pomiary/READOUTS_KAL_60.json')
# time70, thrust70 = prepare_to_plot('pomiary/READOUTS_KAL_70.json')
# fig, ax = plt.subplots()
# ax.plot(time45, thrust45, label='nozzle 45mm', color='red')
# ax.plot(time50, thrust50, color='green', label='nozzle 50mm')
# ax.plot(time55, thrust55, color='blue', label='nozzle 55mm')
# ax.plot(time60, thrust60, color='orange', label='nozzle 60mm')
# ax.plot(time70, thrust70, color='black', label='nozzle 70mm')


time, thrust = prepare_to_plot(input_path)
fig, ax = plt.subplots()
ax.plot(time, thrust, label='one grain', color='red')

ax.set(xlabel='time (ms)', ylabel='thrust (N)',
       title='Chart of the thrust to time')
ax.grid()

plt.legend(frameon=True, loc='upper right', ncol=2)

fig.savefig(output_path)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_13_55_47_with_battery_220_Ohm_interrupted")

df["timestamp"] = df["timestamp"] / 1000
# df = df[df["timestamp"] < 2 * 60]
df["inVoltage"] = df["inVoltage"] / 1000
df["outVoltage"] = df["outVoltage"] / 1000
df["batVoltage"] = df["batVoltage"] / 1000
df = df[df["timestamp"] < 60 * 4]

def set_minute_xaxis(ax):
    ax.xaxis.set_major_formatter(lambda x, pos: f"{int(x)//60:d}хв {int(x)%60:d}c")

fig1 = plt.figure(figsize=(20, 11))

print(df)


ax1 = fig1.add_subplot(3,1,1)
plt.yticks(np.append(np.arange(0, 2.5, 0.5), np.arange(2.6, 3.5, 0.2)))
set_minute_xaxis(ax1)
plt.grid()
plt.ylabel("Напруга, В")
plt.title("Напруга на OUT+")
plt.xlim([0, 60*4])
plt.ylim([0, 3.4])
plt.plot(df["timestamp"], df["outVoltage"])
plt.xticks(np.arange(0, max(df["timestamp"])+1, 30.0))

ax2 = fig1.add_subplot(3,1,2)
plt.yticks(np.append(np.arange(0, 2.5, 0.5), [2.3, 2.9]))
plt.xticks(np.arange(-2, max(df["timestamp"])+1, 16.0))
# set_minute_xaxis(ax2)
ax2.xaxis.set_major_formatter(lambda x, pos: f"{int(x)}c")
plt.grid()
plt.ylabel("Напруга, В")
plt.title("Напруга на IN+")
plt.xlim([0, 60*4])
plt.ylim([0, 3.4])
plt.plot(df["timestamp"], df["inVoltage"])

ax3 = fig1.add_subplot(3,1,3)
plt.xticks(np.arange(0, max(df["timestamp"])+1, 30.0))
# fig1.add_subplot(3,1,3)
# plt.xticks(np.arange(0, max(df["timestamp"])+1, 60.0))
set_minute_xaxis(ax3)
plt.grid()
plt.xlabel("Час", labelpad=5, fontsize=15)
plt.ylabel("Напруга, В")
plt.title("Напруга на BAT+")
plt.xlim([0, 60*4])
plt.ylim([0, 4])
plt.plot(df["timestamp"], df["batVoltage"])


ax1.margins(x=0)
ax2.margins(x=0)
ax3.margins(x=0)
fig1.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)

plt.savefig(fname="img.png", dpi=250)
plt.show()

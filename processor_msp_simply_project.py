import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_00_52_42")

df["timestamp"] = df["timestamp"] / 1000
# df = df[df["timestamp"] < 2 * 60]
df["inVoltage"] = df["inVoltage"] / 1000
df["outVoltage"] = df["outVoltage"] / 1000
df["batVoltage"] = df["batVoltage"] / 1000
df = df[df["timestamp"] < 60 * 9]

working1 = df[df["timestamp"] < 74]
not_working1 = df[(74 <= df["timestamp"]) & (df["timestamp"] < 355)]
plugged_out = df[(355 <= df["timestamp"]) & (df["timestamp"] < 444)]
working2 = df[(444 <= df["timestamp"]) & (df["timestamp"] < 497)]
strange_working = df[(497 <= df["timestamp"]) & (df["timestamp"] < 60 * 12)]

def plot_all_stages(pin: str):
    plt.plot(working1["timestamp"], working1[pin], color="#1F77B4")
    plt.plot(not_working1["timestamp"], not_working1[pin], color="#FF7E0E")
    plt.plot(plugged_out["timestamp"], plugged_out[pin], color="#2CA02C")
    plt.plot(working2["timestamp"], working2[pin], color="#D62728")
    plt.plot(strange_working["timestamp"], strange_working[pin], color="#9467BD")

def set_minute_xaxis(ax):
    ax.xaxis.set_major_formatter(lambda x, pos: f"{int(x)//60:d}хв")

fig1 = plt.figure(figsize=(20, 11))

print(df)


ax1 = fig1.add_subplot(3,1,1)
plt.yticks(np.append(np.arange(0, 2.5, 0.5), np.arange(2.6, 3.5, 0.2)))
set_minute_xaxis(ax1)
plt.grid()
plt.xlabel("time", labelpad=-5)
plt.ylabel("voltage, V")
plt.title("Voltage on OUT+")
plt.ylim([0, 3.4])
plot_all_stages("outVoltage")
plt.xticks(np.arange(0, max(df["timestamp"])+1, 60.0))

color_descr_dict = {
    "#1F77B4" : "Підключив MSP до живлення \n(працює, передає температуру)",
    "#FF7E0E" : "Тут перестало передавати",
    "#2CA02C" : "Відключив MSP від живлення \n(чомусь OUT+ зразу до 3V стрибнув)",
    "#D62728" : "Підключив знову до живлення \n(працює, передає температуру)",
    "#9467BD" : "Чомусь перестало передавати"
}
items = list(color_descr_dict.items())
keys = [item[0] for item in items]
values = [item[1] for item in items]
plt.legend(labels=values, labelcolor=keys, loc="lower left", bbox_to_anchor=(375,-0.05), bbox_transform=ax1.transData)


ax2 = fig1.add_subplot(3,1,2)
plt.xticks(np.arange(0, max(df["timestamp"])+1, 60.0))
set_minute_xaxis(ax2)
plt.grid()
plt.xlabel("time", labelpad=-5)
plt.ylabel("voltage, V")
plt.title("Voltage on IN+")
plt.ylim([0, 3.4])
plot_all_stages("inVoltage")

ax3 = fig1.add_subplot(3,1,3)
plt.xticks(np.arange(0, max(df["timestamp"])+1, 60.0))
# fig1.add_subplot(3,1,3)
# plt.xticks(np.arange(0, max(df["timestamp"])+1, 60.0))
set_minute_xaxis(ax3)
plt.grid()
plt.xlabel("time", labelpad=-5)
plt.ylabel("voltage, V")
plt.title("Voltage on BAT+")
plt.ylim([0, 5.5])
plot_all_stages("batVoltage")

ax1.margins(x=0)
ax2.margins(x=0)
ax3.margins(x=0)
fig1.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)

plt.savefig(fname="img.png", dpi=250)
plt.show()

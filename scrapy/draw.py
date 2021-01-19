# -*- coding:UTF-8 -*-
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["font.sans-serif"]=["simhei"]
matplotlib.rcParams["font.family"]="sans-serif"


plt.bar([1],[147],label=u"bj")
plt.bar([2],[258],label=u"sh")
plt.bar([3],[369],label=u"nj")
plt.bar([4],[123],label=u"sd")
plt.bar([5],[456],label=u"sz")

matplotlib.use("Agg")
plt.savefig("1.jpg")
plt.legend()
#plt.show()

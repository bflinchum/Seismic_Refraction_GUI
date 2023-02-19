import seismicProcessingMethods as spm
import matplotlib.pyplot as plt

#x: number of geophones/ number of columns in data 
#t: starts when sledgehammer hits the ground (normally starts at -5 ms)/ number of rows in data
#data: the actual data (speed or how much the ground has moved)
x, t, data, gx, shotLocation = spm.getData("segy", "70_extracted.sgy")

print(x.shape)
print(t.shape)
print(data.shape)

data = spm.normalizeTraces(data)

fig = plt.figure(1) 
ax = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax.pcolorfast(x,t,data)
ax2.plot(t,data[:, 1])
plt.show()
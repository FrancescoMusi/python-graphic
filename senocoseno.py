import numpy as np
import matplotlib.pyplot as pl

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

fig = pl.figure(figsize=(8, 4))
ax = pl.subplot(111)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

ax.patch.set_edgecolor('k')
ax.patch.set_linewidth(1)

ax.set_xlim(X.min() * 1.1, X.max() * 1.1)
ax.set_ylim(C.min() * 1.1, C.max() * 1.1)

ax.xaxis.set_ticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.xaxis.set_ticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

ax.yaxis.set_ticks([-1, 0, +1])
ax.yaxis.set_ticklabels([r'$-1$', r'$0$', r'$+1$'])

ax.xaxis.set_ticks([-3*np.pi/4, -np.pi/4, np.pi/4, 3*np.pi/4] , minor=True)
ax.yaxis.set_ticks([-0.5, 0.5] , minor=True)

ax.xaxis.set_label_text('$angolo$')
ax.xaxis.set_label_coords( x = 0.5 , y = -0.05)

ax.yaxis.set_label_text('$A$')
ax.yaxis.set_label_coords( x = -0.05 , y = 0.5)

#ax.set_title('$seno e coseno$')

#etichette 
ax.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="coseno")
ax.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="seno")

#legenda
ax.legend(loc='best')

pl.savefig("./senocoseno.png", dpi=800)
pl.show()
import gridpts as gr
import numpy as np
from matplotlib import pyplot as plt

def plot_unifcheb(n):
	assert n%2 == 0
        x = gr.unif(n)
        xx = np.linspace(-1,1,200)*0.99+1e-6
        yy = gr.evalprod(x, xx)
        
        zero = np.array([0]) #nmlz
        yy = yy/gr.evalprod(x, zero)

        plt.subplot(211) 
        plt.plot(xx, yy)
        plt.title('nmlz prod poly with ' + str(n) + ' unif points')
        
        x = gr.cheb(n)
        yy = gr.evalprod(x, xx)
        
        yy = yy/gr.evalprod(x, zero) #nmlz

        
        plt.subplot(212) 
        plt.plot(xx, yy)
        plt.title('nmlz prod poly with ' + str(n) + ' cheb points')
        plt.show()


plot_unifcheb(30)

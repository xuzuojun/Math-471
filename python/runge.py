from matplotlib import pyplot as plt
import lgrng 

def runge(x):
	return 1.0/(1+x*x)

x = lgrng.gr.cheb(200)
xx = lgrng.gr.unif(2000)*0.99+1e-4
lgrng.demo(runge, x, xx) #error will be small

plt.figure()
x = lgrng.gr.unif(60)
lgrng.demo(runge, x, xx) #shows runge phenomenon
plt.show()

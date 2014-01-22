import gridpts
import demo

def runge(x):
	return 1.0/(1+x*x)

x = gridpts.cheb(200)
xx = gridpts.unif(500)*0.99+1e-4
demo.plot(runge, x, xx)

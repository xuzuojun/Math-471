import numpy as np
import lgrng

def evalnfit(f, x, xx):
	"""\
	evalnfit(f, x, xx):
	f = function being tested
	x = grid points
	xx = points for interpolation
	returns y, yy where y = f(x) and yy are interpolated at xx
	"""
	assert isinstance(x, np.ndarray) and isinstance(xx, np.ndarray)
	
	y = np.empty(x.shape)
	for i,g in enumerate(x):
		y[i] = f(x[i])
		
	yy = lgrng.interp(x, y, xx)
	return y, yy

def plot(f, x, xx):
	"""\
	plot(f, x, xx):
	f = function to be interpolated
	x = grid points
	xx = interpolation points
	plots interpolant and returns maximum error
	"""
	from matplotlib import pyplot as plt
	y, yy = evalnfit(f, x, xx)
	plt.plot(x, y, 'ro')
	plt.plot(xx, yy, 'k')
	
	zz = np.zeros(xx.shape)
	for i,xp in enumerate(xx):
		zz[i] = f(xp)
		
	plt.plot(xx, zz, 'b')

	plt.axis('tight')
	plt.xlabel('x')
	plt.ylabel('y')

	zz = np.empty(yy.shape)
	for i,g in enumerate(xx):
		zz[i] = f(xx[i])
	error = np.abs(zz - yy)
	error = np.max(error)
		
	ax = plt.gca()
	plt.text(0.4, 0.2, 'Error = '+str(error), transform=ax.transAxes)
	plt.axis([np.min(x), np.max(x), np.min(y), np.max(y)])
	plt.show()

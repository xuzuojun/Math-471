x = cheb(100)
xx = linspace(-1, 1, 200)*0.99

y = 1.0/(1+x.^2)
n = length(x)
c = newtdd(x, y, n)

yy = zeros(size(xx))
for i=1:length(xx)
  yy[i] = nest(n-1, c, xx[i], x)

plot(x, y, 'ro')
hold on
plot(xx, yy, 'k')
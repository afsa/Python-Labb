%-0.24 minsta lösning, 6 lösningar
clf;
x = -1:0.001:5;
y = x.^2/5 + 1.2*sin(pi.*x)-3.*x.*exp(-x./2);
plot(x, y)
hold on;
plot(x, 0)

f = @(x) x^2/5 + 1.2*sin(pi*x)-3*x*exp(-x/2);
disp(fzero(f, -1))

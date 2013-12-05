clf
hold on
data2

x = toCol(x);
y = toCol(y);
drawArea = getAxis(x, y);

f = leastSquareOrthogonal(x, y);
xp = drawArea(1):0.01:drawArea(2);
plot(xp, f(xp), 'k')
plot(x, y, 'k*')

axis(drawArea);
setGrid();

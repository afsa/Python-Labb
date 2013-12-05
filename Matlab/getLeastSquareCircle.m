function getLeastSquareCircle( x, y )
%Takes cords and returns circle function form least square circle
%   x-cords, y-cords

lengthX = length(x);

if lengthX ~= length(y)
    return ;
end

clf
hold on

drawArea = getAxis(x, y, 0.3);

x = toCol(x);
y = toCol(y);

A = [ones(lengthX, 1) x y];
Y = x.^2 + y.^2;

c = A\Y;

r = sqrt(c(1)+sum(c(2:3).^2)/4);
fx = @(tf) c(2)/2 + r*cos(tf);
fy = @(tf) c(3)/2 + r*sin(tf);

plot(x, y, 'k*')

t = 0:0.01:2*pi;
plot(fx(t), fy(t), 'k')

axis(drawArea)
axis equal
setGrid();

end


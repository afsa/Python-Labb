function leastSquareLinear( x, y )
%Get a least square solution drawn in a graph
%   x is x-values, y is y-values

lengthX = length(x);

if lengthX ~= length(y)
    return
end

x = toCol(x);
y = toCol(y);
drawArea = getAxis(x,y);

clf;
hold on

A = [ones(lengthX, 1) x];
c = A\y;

plot(x, y, '*');
xp = drawArea(1):0.01:drawArea(2);
f = @(xf) c(1)+c(2).*xf;
plot(xp, f(xp));

rmsError = sqrt(lengthX^-1*sum((f(x)-y).^2));

text(min(x), max(y), sprintf('rms error: %.2f', rmsError));

axis(drawArea);

end


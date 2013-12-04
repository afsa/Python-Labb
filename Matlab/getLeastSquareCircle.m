function [ f ] = getLeastSquareCircle( x, y )
%Takes cords and returns circle function form least square circle
%   x-cords, y-cords

lengthX = length(x);

if lengthX ~= length(y)
    f = @(xf) 0;
    return ;
end

x = toCol(x);
y = toCol(y);

A = [ones(lengthX, 1) x y];
Y = [x y].^2;

c = A\Y;




end


function [f] = leastSquareOrthogonal( x, y )
%Least square approximation with orthogonal distances
%   x - x cord, y - y cord

xm = mean(x); ym = mean(y);
xc = x - xm; yc = y - ym;

A = [xc'*xc xc'*yc; xc'*yc yc'*yc];

[v, L] = eig(A);

f = @(xf) -v(1, 1)/v(1, 2)*(xf-xm)+ym;

end


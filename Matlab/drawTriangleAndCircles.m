function drawTriangleAndCircles( x, y )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

lineColorRGB = [0 0 0];
circleColorRGB = [255 255 0];

d = [pdist([x(1) y(1); x(2) y(2)]) pdist([x(2) y(2); x(3) y(3)]) pdist([x(3) y(3); x(1) y(1)])];

r = [1/2*(d(1)-d(2)+d(3)) 1/2*(d(1)+d(2)-d(3)) 1/2*(-d(1)+d(2)+d(3))];

v = 0:0.01:2*pi;

clf;

for i = 1:3
    xc = x(i) + r(i)*cos(v);
    yc = y(i) + r(i)*sin(v);
    fill(xc, yc, circleColorRGB./255)
    hold on;
end

plot([x(1) x(2) x(3) x(1)], [y(1) y(2) y(3) y(1)], 'LineStyle', '--', 'Color', lineColorRGB./255)
end


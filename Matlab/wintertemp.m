clf;
hold on;
load('vinter');

t = vinterdag(:, 1).*60 + vinterdag(:, 2);
T = vinterdag(:, 3);

drawArea = getAxis(t, T);

sinf = @(xs) sin(2*pi.*xs./(60*24));
cosf = @(xc) cos(2*pi.*xc./(60*24));

lengtht = length(t);

t = toCol(t);
T = toCol(T);

A = [ones(length(t), 1) sinf(t) cosf(t)];
c = A\T;

plot(t, T, 'k*');
xp = drawArea(1):0.01:drawArea(2);
f = @(xf) c(1)+c(2).*sinf(xf)+c(3).*cosf(xf);
plot(xp, f(xp), 'k');

text(min(t) + 50, max(T), sprintf('max: %.1f', max(f(xp))));
title('Temperatur under vintern');
xlabel('Tid från midnatt t [minuter]');

axis(drawArea);
setGrid();
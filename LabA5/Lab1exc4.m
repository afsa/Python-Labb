clf;
temp = [600 800 1000 1100];
x = 0:0.001e-6:10e-6;
f = @(l, t) 3.7415e-16./(l.^5.*(exp(0.014388./(l.*t))-1));
for i = 1:4
    plot(x, f(x, temp(i)), 'Color', [0 0 0])
    hold on;
    [val, ind] = max(f(x, temp(i)));
    plot(x(ind), val, '*', 'color', [0 0 0])
    text(x(ind) - 0.3e-6, val + 0.5e9, strcat('T=',sprintf('%3d', temp(i)),'K'));
end
axis([0 1e-5 0 2.5e10])
title('Intensitetskurvor');
xlabel('Våglängd \lambda [m]');

grid on
set(gca,'Xcolor',[0.85 0.85 0.85])
set(gca,'Ycolor',[0.85 0.85 0.85])
copiedAxis = copyobj(gca,gcf);
set(copiedAxis, 'color', 'none', 'xcolor', [0 0 0], 'xgrid', 'off', 'ycolor',[0 0 0], 'ygrid','off');
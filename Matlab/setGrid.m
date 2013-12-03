function setGrid()
%UNTITLED8 Summary of this function goes here
%   Detailed explanation goes here
grid on
set(gca,'Xcolor',[0.85 0.85 0.85])
set(gca,'Ycolor',[0.85 0.85 0.85])
copiedAxis = copyobj(gca,gcf);
set(copiedAxis, 'color', 'none', 'xcolor', [0 0 0], 'xgrid', 'off', 'ycolor',[0 0 0], 'ygrid','off');

end


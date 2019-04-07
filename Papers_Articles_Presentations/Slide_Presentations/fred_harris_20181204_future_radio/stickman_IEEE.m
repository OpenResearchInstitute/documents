
figure(2) 
del=150;
d1=[0  1  2  3  4  5  6  7  8  9  10  9  8  7  6  5  4  3  2  1];
d2=[0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1];
d3=[10 9  8  7  6  5  4  3  2  1  0   1  2  3  4  5  6  7  8  9];
d4=[0  1  2  3  4  5  6  7  8  9  10  9  8  7  6  5  4  3  2  1]/3;
ang=0:0.01:2*pi; r=5;
xp=r*cos(ang);
yp=3*r*sin(ang);
flg=1;
for k=1:415
    clf
%proj4_circle(0-del,165,5); % Head

% ang=0:0.01:2*pi; r=5;
% xp=r*cos(ang);
% yp=3*r*sin(ang);
fill(0-del+xp,165+yp, 'k', 'linewidth', 2);
hold on
grid on
xlim([-200 200])
ylim([0 500]*0.6)

x = [0-del, 0-del]; % Neck
y = [140, 150];
plot(x,y, 'k', 'linewidth', 3)
hold on
grid on
xlim([-200 200])
ylim([0 500]*0.6)

x = [0-del, 0-del]; % Body
y = [75, 140];
plot(x,y, 'k', 'linewidth', 3)
hold on
grid on
xlim([-200 200])
ylim([0 500]*0.6)

x1 = [0-del, 0-del+d1(flg)]; % Right arm
y1 = [140, 80+d1(flg)];
plot(x1,y1, 'k', 'linewidth', 3)
grid on
xlim([-200 200])
ylim([0 500]*0.6)

x1 = [-0-del+d2(flg), 0-del]; % Left arm
y1 = [80-d2(flg), 140];
plot(x1,y1, 'k', 'linewidth', 3)
grid on
xlim([-200 200])
ylim([0 500]*0.6)

x1 = [0-del, 0-del+d1(flg)]; % Right leg
y1 = [75, 0+d4(flg)];
plot(x1,y1, 'k', 'linewidth', 3)
hold on
x2 = [0-del+d1(flg), 6-del+d1(flg)];
y2 = [0+d4(flg), 0+d4(flg)];
plot(x2,y2, 'k', 'linewidth', 3)
grid on
xlim([-200 200])
ylim([0 500]*0.6)

x1 = [-0-del+d2(flg), 0-del]; % Left leg
y1 = [0+d4(flg), 75];
plot(x1,y1, 'k', 'linewidth', 3)
hold on
x2 = [-0-del+d2(flg), 6-del+d2(flg)];
y2 = [0+d4(flg), 0+d4(flg)];
plot(x2,y2, 'k', 'linewidth', 3)
grid on
xlim([-200 200])
ylim([0 500]*0.6)
title('Come Walk With Me. We are going to the San Diego IEEE Signal Processing and Communications Society meeting','fontsize',18)
pause(0.01)
if k<300
del=del-1;
else
    del=del+1;
end
flg=flg+1;
if flg>=20
   flg=1;
end
end
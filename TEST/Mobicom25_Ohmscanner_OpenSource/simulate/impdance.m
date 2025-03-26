close all
clear all

%% ============================ capAndImpedace ================================
filePath = './impedanceWithCapcity.csv';
data = readmatrix(filePath);
data = data(2:end, :);
freList = data(:, 1);
data(:, 1) = [];
capList = 0.5 : 0.1 : 1.5;
re = data(freList == 0.92, 1:length(capList));
im = data(freList == 0.92, length(capList)+1:end);

figure
yyaxis left
plot(capList, re, '-*','LineWidth', 2)
ylabel('Real part of impedance (\Omega)', 'fontsize',22,'fontname','Arial','FontWeight','normal');
yyaxis right
plot(capList, im, '-*', 'LineWidth', 2)
ylabel('Imaginary part of impedance (\Omega)')
xlabel('Capacitance (pF)', 'fontsize',22,'fontname','Arial','FontWeight','normal');
title('Impedance with different capacitance')
set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
ld = legend('Real', 'Imag');
ld.Box = 'off';
RFS([1.6, 1.6]);

%% ============================ buttonPosAndImpedace ================================
filePath = './impedanceWithButtonPos.csv';
data = readmatrix(filePath);
data = data(2:end, :);
freList = data(:, 1);
data(:, 1) = [];
moveDistance = 5 : 5 : 40;
re = data(freList == 0.92, 1:length(moveDistance));
im = data(freList == 0.92, length(moveDistance)+1:end);

figure
yyaxis left
plot(1:length(moveDistance), re, '-*','LineWidth', 2)
ylabel('Real part of impedance (\Omega)', 'fontsize',22,'fontname','Arial','FontWeight','normal');
yyaxis right
plot(1:length(moveDistance), im, '-*', 'LineWidth', 2)
ylabel('Imaginary part of impedance (\Omega)')
xlabel('Position', 'fontsize',22,'fontname','Arial','FontWeight','normal');
title('Impedance with different capacitance')
set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
ld = legend('Real', 'Imag');
ld.Box = 'off';
RFS([1.6, 1.6]);


%% ============================ raoteAngleAndImpedace ================================
filePath = './impedanceWithRoate.csv';
data = readmatrix(filePath);
data = data(2:end, :);
freList = data(:, 1);
data(:, 1) = [];
roateAngle = 0 : 15 : 75;
re = data(freList == 0.92, 1:length(roateAngle));
im = data(freList == 0.92, length(roateAngle)+1:end);

figure
yyaxis left
plot(roateAngle, re, '-*','LineWidth', 2)
ylabel('Real part of impedance (\Omega)', 'fontsize',22,'fontname','Arial','FontWeight','normal');
yyaxis right
plot(roateAngle, im, '-*', 'LineWidth', 2)
ylabel('Imaginary part of impedance (\Omega)')
xlabel('Roate Angle(deg)', 'fontsize',22,'fontname','Arial','FontWeight','normal');
title('Impedance with different capacitance')
set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
ld = legend('Real', 'Imag');
ld.Box = 'off';
RFS([1.6, 1.6]);
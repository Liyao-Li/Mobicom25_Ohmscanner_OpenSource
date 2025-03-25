close all
clear all

%% ============================ capAndImpedace ================================
filePath = './impedanceWithCapcity.csv';
data = readmatrix(filePath);
data = data(2:end, :);
freList = data(:, 1);
capList = 0.5 : 0.1 : 1.5;
re = data(freList == 0.922, 1:length(capList));
im = data(freList == 0.922, length(capList)+1:end);


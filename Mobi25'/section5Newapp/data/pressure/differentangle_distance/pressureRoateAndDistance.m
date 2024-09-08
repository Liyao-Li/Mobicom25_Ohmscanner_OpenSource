close all;
clear all;

floderPath = '.\压力\roate';
floderInfo = dir(floderPath);
fileNames = {floderInfo.name};
fileNames = fileNames(3:end);

pressureFileNames = fileNames(contains(fileNames, 'csv'));
SCFileNames = fileNames(contains(fileNames, 'txt'));

lengendNames = cell(1, length(SCFileNames));
for i = 1:length(SCFileNames)
    lengendNames{i} = SCFileNames{i}(1:end-4);
end

allSCData = cell(1, length(SCFileNames));
allPressureData = cell(1, length(pressureFileNames));

for i = 1:length(SCFileNames)
    tempData = readAllDataFromFile(fullfile(floderPath, SCFileNames{i}));
    allSCData{i} = tempData{5};
    SCTime = cellfun(@convertTimeStrToSeconds, tempData{8});
    SCTime = SCTime - SCTime(1);
    [allPressureData{i}, pressureTime] = readPressureFromCSV(fullfile(floderPath, pressureFileNames{i}));
    allPressureData{i} = allPressureData{i} - allPressureData{i}(1);

    % 对preeureData进行降采样
    downSampleRate = floor(length(allPressureData{i}) / length(SCTime));
    allPressureData{i} = downsample(allPressureData{i}, downSampleRate);
    pressureTime = downsample(pressureTime, downSampleRate);

    % 对pressureData进行插值
    time = unique([pressureTime; SCTime]);
    time = sort(time);
    allSCData{i} = double(allSCData{i});
    allPressureData{i} = interp1(pressureTime, allPressureData{i}, time);
    allSCData{i} = interp1(SCTime, allSCData{i}, time, 'nearest');
    % 去除NA值
    allPressureData{i}(isnan(allSCData{i})) = [];
    allSCData{i}(isnan(allSCData{i})) = [];
    allSCData{i}(isnan(allPressureData{i})) = [];
    allPressureData{i}(isnan(allPressureData{i})) = [];
end

%% =================== 压力SC曲线 ===================
figure;
hold on;
for i = 1:length(SCFileNames)
    plot(allSCData{i}, allPressureData{i}, LineWidth = 2);
end
ld = legend(lengendNames);
ld.Box = 'off';

grid on;
set(gca, 'GridAlpha', 0.3);  % 设置透明度
set(gca,'GridLineStyle','--');

set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
ylabel('Pressure (N)', 'fontsize',22,'fontname','Arial','FontWeight','normal');
xlabel('Register Value','fontsize',22,'fontname','Arial','FontWeight','normal');
box off;
ax = gca;

set(ax, 'box', 'off', 'TickDir', 'out', 'XMinorTick', 'on', 'YMinorTick', 'on')
% set(ax, 'XTick', ax.XTick, 'fontsize',22,'fontname','Arial','FontWeight','normal');
% set(ax, 'YTick', ax.YTick, 'fontsize',22,'fontname','Arial','FontWeight','normal');
set(ax, 'TickDir', 'in');

ld = legend(lengendNames);
ld.Box = 'off';

aspectRatio = [8.02, 4.57,0.780091086761645];
pbaspect(aspectRatio);

ax.LineWidth = 2;

%% =================== cdf ===================

% 拟合并计算差值
p = polyfit(allSCData{1}, allPressureData{1}, 3);
allEstimatedPressureData = cell(1, length(SCFileNames));
for i = 1 : length(SCFileNames)
    allEstimatedPressureData{i} = polyval(p, allSCData{i});
end

allErrorPressureData = cell(1, length(SCFileNames));
for i = 1 : length(SCFileNames)
    allErrorPressureData{i} = abs(allPressureData{i} - allEstimatedPressureData{i});
end
rota = [0 20 40 60]
figure;
hold on;
for i = 1:length(SCFileNames)
    A_error=[];
    [yData, xData] = ecdf(allErrorPressureData{i});
A_error =   allErrorPressureData{i}
fid = fopen(['rotate-error' num2str(rota(i)) '.txt'], 'a+');%' num2str(ante) '
for ii = 1:length(A_error)
        fprintf(fid,'%f',A_error(ii)); 
        fprintf(fid,'\t');
        fprintf(fid,'\n');
%         fclose(fid);
end
fclose(fid);

    plot(xData, yData, '-','LineWidth',3);
end

set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
    
grid on;
set(gca, 'GridAlpha', 0.3);  % 设置透明度
set(gca,'GridLineStyle','--');

xlabel('Pressure (N)','fontsize',22,'fontname','Arial','FontWeight','normal');
ylabel('CDF','fontsize',22,'fontname','Arial','FontWeight','normal');

box off;
ax = gca;

set(ax, 'box', 'off', 'TickDir', 'out', 'XMinorTick', 'on', 'YMinorTick', 'on')
% set(ax, 'XTick', ax.XTick, 'fontsize',22,'fontname','Arial','FontWeight','normal');
% set(ax, 'YTick', ax.YTick, 'fontsize',22,'fontname','Arial','FontWeight','normal');
set(ax, 'TickDir', 'in');

ld = legend(lengendNames);
ld.Box = 'off';

aspectRatio = [8.02, 4.57,0.780091086761645];
pbaspect(aspectRatio);

ax.LineWidth = 2;

% 处理TimeStr的自定义函数
function timeInSeconds = convertTimeStrToSeconds(timeStr)
    parts = strsplit(timeStr, ' ');
    timeStr = parts{1};
    timeInSeconds = str2double(timeStr(1:2)) * 3600 + str2double(timeStr(3:4)) * 60 + str2double(timeStr(5:6)) + 0.001 * str2double(timeStr(7:9));
end
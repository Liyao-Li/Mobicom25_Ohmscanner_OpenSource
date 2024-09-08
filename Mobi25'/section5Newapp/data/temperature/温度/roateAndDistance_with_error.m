% close all;
clear all;

floderPath = '.\roate';
fldoerInfo = dir(floderPath);
floderNames = {fldoerInfo.name};
floderNames = floderNames(3:end);
floderNames = sortByNumber(floderNames);

for i = 1 : length(floderNames)
    fileInfo = dir(fullfile(floderPath, floderNames{i}));
    fileNames = {fileInfo.name};
    fileNames = fileNames(3:end);
    fileNames = sortByNumber(fileNames);
    if i == 1
        allSCData = cell(length(floderNames), length(fileNames));
        temperature = zeros(1, length(fileNames));
        for j = 1 : length(fileNames)
            temperature(j) = str2double(fileNames{j}(1:end-4));
        end
    end
    for j = 1 : length(fileNames)
        allSCData{i, j} = readSCFromFile(fullfile(floderPath, floderNames{i}, fileNames{j}));
    end
end

%% ======================================== 平均 =====================================
meanAllSCData = cellfun(@(x) mean(x), allSCData);

figure;
hold on;
for i = 1 : size(meanAllSCData, 1)
    plot(temperature, meanAllSCData(i, :), '-*', LineWidth=2);
end

set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
ylabel('Register Value','fontsize',22,'fontname','Arial','FontWeight','normal');
xlabel('Temperature','fontsize',22,'fontname','Arial','FontWeight','normal');

box off;
ld = legend(floderNames);
ld.Box = 'off';
ax = gca;
ax.LineWidth = 2;

%% ==================================== cdf =========================================
p = polyfit(meanAllSCData(1, :), temperature, 3);
estimateTemperatureData = zeros(size(meanAllSCData));
for i = 1 : length(floderNames)
    estimateTemperatureData(i, :) = polyval(p, meanAllSCData(i, :));
end
allEstimateTemperatureData = cell(length(floderNames), 15);
allTrueTemperatureData = cell(length(floderNames), 15);
dist=[50 100 150 200]
for i = 1 : size(allSCData, 1)
    for j = 1 : size(allSCData, 2)
        allEstimateTemperatureData{i, j} = polyval(p, double(allSCData{i, j}));
        allTrueTemperatureData{i, j} = ones(size(allSCData{i, j})) * temperature(j);
    end
end
allErrorTemperatureData = cell(length(floderNames), 15);
for i = 1 : size(allTrueTemperatureData, 1)
    for j = 1 : size(allTrueTemperatureData, 2)
        allErrorTemperatureData{i, j} = abs(double(allTrueTemperatureData{i, j}) - allEstimateTemperatureData{i, j});
    end
end

allHorzatErrorTemperatureData = cell(size(allErrorTemperatureData, 1), 1);
for i = 1 : size(allErrorTemperatureData, 1)
    allHorzatErrorTemperatureData{i} = vertcat(allErrorTemperatureData{i, :});
end
% 绘制CDF
figure;

for i = 1 : length(allHorzatErrorTemperatureData)
    [yData, xData] = ecdf(allHorzatErrorTemperatureData{i});
    % fid = fopen([path '/B-' num2str(kk) '.txt'], 'a+');%' num2str(ante) '
    A_error = allHorzatErrorTemperatureData{i}
    % delete('differentdisSC3.txt')
% fid = fopen(['dis-error' num2str(dist(i)) '.txt'], 'a+');%' num2str(ante) '
% for ii = 1:length(A_error)
%         fprintf(fid,'%f',A_error(ii)); 
%         fprintf(fid,'\t');
%         fprintf(fid,'\n');
% %         fclose(fid);
% end
% fclose(fid);
    plot(xData, yData, '-','LineWidth',3);
    hold on;
end
set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
   
grid on;
set(gca, 'GridAlpha', 0.3);  % 设置透明度
set(gca,'GridLineStyle','--');

xlabel('Temperature ()','fontsize',22,'fontname','Arial','FontWeight','normal');
ylabel('CDF','fontsize',22,'fontname','Arial','FontWeight','normal');

box off;
ax = gca;

set(ax, 'box', 'off', 'TickDir', 'out', 'XMinorTick', 'on', 'YMinorTick', 'on')
% set(ax, 'XTick', ax.XTick, 'fontsize',22,'fontname','Arial','FontWeight','normal');
% set(ax, 'YTick', ax.YTick, 'fontsize',22,'fontname','Arial','FontWeight','normal');
set(ax, 'TickDir', 'in');
xlim([0, 10]);

ld = legend(floderNames);
ld.Box = 'off';

aspectRatio = [8.02, 4.57,0.780091086761645];
pbaspect(aspectRatio);

ax.LineWidth = 2;
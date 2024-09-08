close all;
clear all;
clc;

allFloderPath = '.\differencialtag\distance\0.5cm\2.5cm';
allFloderInfo = dir(allFloderPath);
allFloderName = {allFloderInfo.name};
allFloderName = allFloderName(~ismember(allFloderName,{'.','..'}));
allFloderName = sortByNumber(allFloderName);
allRoateData = zeros(length(allFloderName), 6);

for allFloderIndex = 1 : length(allFloderName)
    fileInfo = dir([allFloderPath, '\', allFloderName{allFloderIndex}]);
    disp([allFloderPath, '\', allFloderName{allFloderIndex}]);
    fileName = {fileInfo.name};
    fileName = fileName(~ismember(fileName,{'.','..'}));
    fileName = sortByNumber(fileName);
    % 开始读
    for fileIndex = 1 : length(fileName)
        data = readSCFromFile([allFloderPath, '\', allFloderName{allFloderIndex}]);
        data(data == 0)=[];
        % allRoateData(allFloderIndex, fileIndex) = mode(data);
        modeData(allFloderIndex, fileIndex) = mode(data);
        maxData(allFloderIndex, fileIndex) = max(data);
        minData(allFloderIndex, fileIndex) = min(data);
    end
end

figure  
% 创建一个包含所需 x 轴刻度的向量  
xTicks = [50 100 150 200 250 300 320 350 400 450 500 550 570];  
% xTicks = [50 100 150 200 250 300 320];
plot( modeData, '-*', 'LineWidth', 2);  

errora = maxData-minData;
% figure  
% hold on; % 将 hold on 放在循环外部，以避免每次绘制时都重新打开 hold  
% for i = 1 : length(allFloderName)  
%     % 假设每个文件索引对应一个 xTicks 值（从 1 开始索引）  
%     xData = xTicks(1:length(fileName)); % 这里假设 length(fileName) 与 xTicks 的一部分相匹配  
%     yData = allRoateData(i, 1:length(fileName)); % 对应的 y 数据  
% 
%     % 绘制数据，使用 xData 作为 x 轴的值  
%     plot(xTicks, yData, '-*', 'LineWidth', 2);  
% end  
  
% % 设置 x 轴刻度和标签  
% set(gca, 'XTick', xTicks, 'XTickLabel', num2str(xTicks).');  
  
% 设置其他图形属性  
set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');    
xlabel('distance(cm)');    
ylabel('SC');    
grid on;  
% legend({"1", "2", "3", "4", "5", "6", "7"});
figure
plot(modeData,'*-')
errorbar(xTicks,modeData,errora/2)




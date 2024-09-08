close all;
clear all;

floderPath = '.\distance';
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

meanAllSCData = zeros(size(allSCData, 1), size(allSCData, 2));
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

close all
clear all

fid = fopen('path1','rb');
data = fread(fid,'float32');
freList = 500 : 20 : 1000;

data(1:end-1);
I = data(1:2:end);
Q = data(2:2:end);
x_1 = I + 1i*Q;

figure
plot(abs(x_1));   

% EPC or RN16 index within the first file
signal = abs(x_1(index1:index2));
findsignal(abs(x_1), signal, "Maxdistance", 1);
%% ==================================================================================

allFloderPath = 'path2';
allFloderInfo = dir(allFloderPath);
allFileNames = {allFloderInfo.name};
allFileNames = allFileNames(~ismember(allFileNames,{'.','..'}));
allFileNums = length(allFileNames);
for fileIndex = 1 : allFileNums
    if exist([allFileNames{fileIndex} '.txt'], 'file')
        continue;
    end
    floderPath = [allFloderPath, allFileNames{fileIndex}];
    fileFloderInfo = dir(floderPath);

    fileNum = length(fileFloderInfo) - 2;
    fileNames = {fileFloderInfo.name};
    fileNames = fileNames(~ismember(fileNames,{'.','..'}));

    % Record the phase and amplitude of different fre
    differentFrePhase = [];
    differentFreAmplitude = [];

    % Traverse all folders
    for i = 1 : fileNum
        fileName = fileNames{i};
        filePath = [floderPath '\' fileName];
        disp(filePath);
        fid = fopen([filePath '\source'],'rb');
        data = fread(fid,'float32');
        data(1:end-1);
        I = data(1:2:end);
        Q = data(2:2:end);
        x_1 = I + 1i*Q;
        [sourceSignalStartIndex, sourceSignalEndIndex] = findsignal(abs(x_1), signal);
        
        % Record the start and end indexes of similar signals in the signal
        sameSignalStartIndex = [];
        sameSignalStopIndex = [];
        Maxdistance = 0.5;
        while(length(sameSignalStartIndex) < 20)
            [sameSignalStartIndex, sameSignalStopIndex] = findsignal(abs(x_1), abs(x_1(sourceSignalStartIndex:sourceSignalEndIndex)), "Maxdistance", Maxdistance);
            Maxdistance = Maxdistance + 0.5;
        end
        if(length(sameSignalStartIndex) > 300)
            sameSignalStartIndex = sameSignalStartIndex(1:300);
            sameSignalStopIndex = sameSignalStopIndex(1:300);
        end
        disp("findSignal Done!");
        fid = fopen([filePath  '\outband_source'],'rb');
        data = fread(fid,'float32');
        data(1:end-1);
        I = data(1:2:end);
        Q = data(2:2:end);
        x_1 = I + 1i*Q;
        
        % Used to record detailed signal phase and amplitude
        allPhase = zeros(length(sameSignalStartIndex), 1);
        allAmplitude = zeros(length(sameSignalStartIndex), 1);

        for j = 1 : length(sameSignalStartIndex)
            if(sameSignalStopIndex(j) < length(I))
                tempI = I(sameSignalStartIndex(j):sameSignalStopIndex(j));
                tempQ = Q(sameSignalStartIndex(j):sameSignalStopIndex(j));
    
                % Find the I/Q cluster center of the current signal
                [cluster_idx, center] = kmeans([tempI, tempQ], 2);
                % Calculate Phase
                vector = center(1,:) - center(2,:);
                allPhase(j) = atan2(vector(2), vector(1));
                % Converts a phase less than 0 to a positive number
                if allPhase(j) < 0
                    allPhase(j) = allPhase(j) + pi;
                end
    
                % Calculate the amplitude of a signal
                allAmplitude(j) = norm(vector(2) - vector(1));
            end
        end
        
        differentFrePhase(i) = mean(allPhase);
        differentFreAmplitude(i) = mean(allAmplitude);
    end

    % The 1GHz folder will be read first
    differentFreAmplitude = [differentFreAmplitude(2:end), differentFreAmplitude(1)];
    differentFrePhase = [differentFrePhase(2:end), differentFrePhase(1)];

    differentFrePhase(differentFrePhase == 0) = [];
    differentFreAmplitude(differentFreAmplitude == 0) = [];

    % figure
    % subplot(2,1,1)
    % plot(freList, differentFrePhase, '-*', LineWidth=2);
    % set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
    % ylabel("Phase")
    % xlabel("Frequency (MHz)")

    % subplot(2,1,2)
    % plot(freList, differentFreAmplitude, '-*', LineWidth=2);
    % set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');
    % ylabel("Amplitude")
    % xlabel("Frequency (MHz)")

    fid = fopen([allFileNames{fileIndex} '.txt'], 'w');
    fclose(fid);
    writematrix([freList',differentFreAmplitude',differentFrePhase'], [allFileNames{fileIndex} '.txt']);
end

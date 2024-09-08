% close all;
clear all;
clc;

allFloderPath = '.\differentdistancenew';
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
        modeData(allFloderIndex, fileIndex) = mean(data);
        maxData(allFloderIndex, fileIndex) = max(data);
        minData(allFloderIndex, fileIndex) = min(data);
    end
end


% modeData(5) =(modeData(4)+modeData(6))/2
% modeData(9) =(modeData(8)+modeData(10))/2
% modeData(20) =(modeData(19)+modeData(21))/2
% modeData(1)=[]
% modeData(1)=[]
% modeData(16:17) = modeData(16:17)+8
% modeData = modeData-80

errora = maxData-minData;
% errora(1) = [];
% errora(1) = [];
% errora(10)=2
% errora(11)=2
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
% modeData(17)=160
% modeData(13)=(modeData(12)+modeData(14))/2
% modeData(15)=(modeData(14)+modeData(16))/2
% modeData(5)=(modeData(4)+modeData(6))/2
% modeData(9)=(modeData(8)+modeData(10))/2
% modeData(20)=(modeData(19)+modeData(21))/2
% modeData(24)=(modeData(23)+modeData(25))/2
% modeData(26)=164
% modeData(1)=[]
% errora(1)=[]
% modeData = modeData-2
% modeData(22)=modeData(22)+2;
% modeData(23)=modeData(23)+3
% modeData(24)=modeData(24)+1
% 设置其他图形属性  
set(gca, 'FontSize', 22, 'Fontname', 'Arial', 'FontWeight', 'normal');    
xlabel('distance(cm)');    
ylabel('SC');    
grid on;  
% legend({"1", "2", "3", "4", "5", "6", "7"});
% 20:20:540
% xTicks = [ 40 60 80 90	100	120	140	160	180	200	220	240	260	280	300	320	340	360	380	400	420	440	460	480	500	520	540]
figure
plot(modeData,'*-')
% errorbar(xTicks,modeData,errora/2)
figure  
plot(modeData, '-*', 'LineWidth', 2);  

f=920e6;
V = 0.8;
cp = 1.9:1/484:2.9;
cp = cp*10^(-12);
rp = 2073;
Rs = rp./(1+(2*pi*f*rp.*cp).^2);
Cs = (1+(2*pi*f*rp.*cp).^2)./((2*pi*f*rp)^2.*cp);
Zant = 2.78+72.1159*j;
Zchip = Rs - j*(1./(2*pi*f.*Cs));
[XX,YY] = meshgrid(real(Zchip),imag(Zchip));
X = Rs;
Y = -j*(1./(2*pi*f.*Cs));
Zchip = XX+j*YY;
% [xTicks',modeData,errora,KKKK]
modeData = ceil(modeData)
register = 6:1:490;
impedance = Zchip(modeData)
KKKK = abs(impedance)

% % delete('differentdisSC2.txt')
% % fid = fopen(['differentdisSC2.txt'], 'a+');%' num2str(ante) '
% % for ii = 1:length(modeData)
% %         fprintf(fid,'%f',xTicks(ii)); 
% %         fprintf(fid,'\t');
% %         fprintf(fid,'%f',modeData(ii)); 
% %         fprintf(fid,'\t');
% %         fprintf(fid,'%f',errora(ii)); 
% %         fprintf(fid,'\t');
% %         fprintf(fid,'%f',KKKK(ii)); 
% %         fprintf(fid,'\t');
% %         fprintf(fid,'\n');
% % %         fclose(fid);
% % end
% % fclose(fid); 
% figure
% plot(register,abs(Zchip),'LineWidth',1.5);
% box on
% grid on
% ax = gca;
% ax.XMinorGrid = 'on';
% ax.YMinorGrid = 'on';
% set(gca, 'FontSize', 18, 'Fontname', 'Arial', 'FontWeight', 'normal');
% % xlabel('Real Z_{chip}','fontsize',18,'fontname','Arial','FontWeight','normal');
% ylabel('Z_{chip}','fontsize',18,'fontname','Arial','FontWeight','normal');
% xlabel('register value','fontsize',18,'fontname','Arial','FontWeight','normal');


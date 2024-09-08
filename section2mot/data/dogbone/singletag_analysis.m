
clear all
% close all
clc
% dis = 0:10:90
% dis = 0.5:0.5:5
dis = 90;
% for kk = 1:length(dis)
% path = ['.\chang\' num2str(dis(kk)) '\']
% path = 'rotation'
path = ['.\rotation\' num2str(dis)]
ang =1:1:9;
for k =1:length(ang)
% fid=fopen('.\0.4\60cm\DAntenna1new.txt','wt');      %新建一个txt文件  
% phns = ['.\0.35\60cm\PAntenna1.txt'];                 %要读取的文档所在的路径  
% phns = ['.\3\20cm加压.txt']; 
phns = [path '\' num2str(ang(k)) '.txt']; 
fpn = fopen (phns, 'rt');           %打开文档  
i=1;
% Sensor = strings(6000,4);
while feof(fpn) ~= 1                %用于判断文件指针p在其所指的文件中的位置，如果到文件末，函数返回1，否则返回0  
      file = fgetl(fpn);            %获取文档第一行  
                                   %%%                                  
     new_str=file;              %中间这部分是对读取的字符串file进行任意处理  
     A = split(file);

     if length(A)==8
     phase(i) = cellfun(@str2num,A(1));
     RSSI(i) = cellfun(@str2num,A(2));
     % Sensor(i,:) = char(A(5));

     minutes(i) = cellfun(@str2num,A(6));
     second(i) = cellfun(@str2num,A(7));

     flag(i) = length(A);   
     i=i+1;
     end%%%  
    
%      fprintf(fid,'%s\n',new_str);%新的字符串写入当新建的txt文档中  
%       fprintf(fid,'%s\n',length(file));
end  

for i=1:length(phase)-1
if phase(i+1)-phase(i)>5
    phase(i+1) = phase(i+1)-pi*2;
else if phase(i+1) -phase(i)> 2.5
        phase(i+1) =  phase(i+1)-pi;
else if phase(i+1)-phase(i)<-4.5
        phase(i+1) = phase(i+1)+pi*2;
else if phase(i+1)-phase(i)<-2.5
    phase(i+1) = phase(i+1)+pi;
end
end
end
end
end
phase(find(phase>3)) = phase(find(phase>3))-pi;
%% mean_phase Mean_rss


% mean_phase(k) = mode(phase(length(phase)/4:length(phase)*3/4));
% var_phase(k) = var(phase(length(phase)/4:length(phase)*3/4));
% bar_phase(k) = max(phase(length(phase)/4:length(phase)*3/4))-min(phase(length(phase)/4:length(phase)*3/4));
mean_phase(k) = mean(phase(1:70));
var_phase(k) = var(phase(1:70));
bar_phase(k) = max(phase(1:70))-min(phase(1:70));
mean_RSSI(k) = mean(RSSI(1:70));
var_RSSI(k) = var(RSSI(1:70));
bar_RSSI(k) = max(RSSI(1:70))-min(RSSI(1:70));

% mean_RSSI(k) = mode(RSSI(length(phase)/4:length(phase)*3/4));
% var_RSSI(k) = var(RSSI(length(phase)/4:length(phase)*3/4));
% bar_RSSI(k) = max(RSSI(length(phase)/4:length(phase)*3/4))-min(RSSI(length(phase)/4:length(phase)*3/4));
%  fclose(fid);  
%     minutes=minutes*60*1000;
%     sec = second*1000;
    % time = second;%minutes+sec;
    % T=(time-time(1))/1000;
    % y=hex2dec(Sensor);
% hold on
    figure
plot(phase,'Linewidth',1.5)
% % plot(y,'Linewidth',1.5)
% % plot(T,y(1:length(T)),'Linewidth',1.5)
% % xlim([1,length(y)]);
% % ylim([300,490]);
% set(gca,'FontSize',15,'FontWeight','normal')
% ylabel('Sensor Code','fontsize',15);
% xlabel('Times(s)')
% grid on

mean_phase(find(mean_phase>2.8)) = mean_phase(find(mean_phase>2.8)) -pi;
mean_phase = mean_phase-min(mean_phase)

fid = fopen(['rote' num2str(dis) '-' num2str(ang(k))  '.txt'], 'a+');
for i=1:length(phase)
    fprintf(fid,'%f',phase(i)); 
    fprintf(fid,'\t');
    fprintf(fid,'%f',RSSI(i)); 
    fprintf(fid,'\n');
end
fclose(fid);

end


% figure
% plot(ang,mean_phase,'*-');
% hold on
% errorbar(ang,mean_phase,bar_phase/2,'*')
% title(num2str(dis(kk)))
% saveppt('C:\Users\Liyao\Desktop\A.pptx')
% 
% fid = fopen(['.\rotation-H' num2str(dis(kk)) '.txt'], 'a+');
% fid = fopen(['baseline2.txt'], 'a+');
% for i=1:length(ang)
%     % fprintf(fid,'%f',ang(i)); 
%     % fprintf(fid,'\t');
%     fprintf(fid,'%f',mean_phase(i)); 
%     fprintf(fid,'\t');
% % %     fprintf(fid,'%f',bar_phase(i)); 
% % %     fprintf(fid,'\t');
% % %     fprintf(fid,'%f',mean_RSSI(i)); 
% % %     fprintf(fid,'\t');
% % %     fprintf(fid,'%f',bar_RSSI(i)); 
% % %     fprintf(fid,'\t');
% % %     fprintf(fid,'\n');
% end
% fclose(fid);


% end
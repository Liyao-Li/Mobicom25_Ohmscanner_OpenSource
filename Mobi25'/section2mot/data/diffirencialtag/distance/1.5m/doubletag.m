clear all
% close all
clc
path = 'height\150\'
for kk=1:9
a=load([path num2str(kk) '.txt']);

tagID = unique(a(:,5));
a(find(a(:,5) == tagID(1)),1);
data_a = a(find(a(:,5) == tagID(1)),:);
data_b = a(find(a(:,5) == tagID(2)),:);
% milisecond
timea = data_a(:,7);
timeb = data_b(:,7);

time_new = union(timea,timeb);

phasea = data_a(:,1);
phaseb = data_b(:,1);
% criterion=2.8;
RSSa = data_a(:,2);
RSSb = data_b(:,2);


for i=1:length(phasea)-1
if phasea(i+1)-phasea(i)>5
    phasea(i+1) = phasea(i+1)-pi*2;
else if phasea(i+1) -phasea(i)> 2.5
        phasea(i+1) =  phasea(i+1)-pi;
else if phasea(i+1)-phasea(i)<-4.5
        phasea(i+1) = phasea(i+1)+pi*2;
else if phasea(i+1)-phasea(i)<-2.5
    phasea(i+1) = phasea(i+1)+pi;
end
end
end
end
end
for i=1:length(phaseb)-1
if phaseb(i+1)-phaseb(i)>5
    phaseb(i+1) = phaseb(i+1)-pi*2;
else if phaseb(i+1) -phaseb(i)> 2.5
        phaseb(i+1) =  phaseb(i+1)-pi;
else if phaseb(i+1)-phaseb(i)<-4.5
        phaseb(i+1) = phaseb(i+1)+pi*2;
else if phaseb(i+1)-phaseb(i)<-2.5
    phaseb(i+1) = phaseb(i+1)+pi;
end
end
end
end
end
phase_hopa = phasea;
% % timea = [time_new(1);timea];
% % phase_hopa = [phasea(1)-0.001;phasea];
phase_hopb = phaseb;
% % timeb = [time_new(1);timeb];
% % phase_hopb = [phaseb(1)-0.001;phaseb];
% phase_hopa = phasehopprocess(phasea,criterion);
% phase_hopb = phasehopprocess(phaseb,criterion);
% while max(phase_hopa)-min(phase_hopa)>2.5
%     criterion = criterion-0.2;
%     phase_hopa = phasehopprocess(phase_hopa,criterion);
% end
% while max(phase_hopb)-min(phase_hopb)>2.5
%     criterion = criterion-0.2;
%     phase_hopb = phasehopprocess(phase_hopb,criterion);
% end
cirtific = pi;
phase_hopa_a = interp1(timea,phase_hopa,time_new,"linear",'extrap');
phase_hopa_b = interp1(timeb,phase_hopb,time_new,"linear",'extrap');
RSS_hopa_a = interp1(timea,RSSa,time_new,"linear",'extrap');
RSS_hopa_b = interp1(timeb,RSSb,time_new,"linear",'extrap');
while length(find(phase_hopa_a>cirtific)) > 1;
    phase_hopa_a(find(phase_hopa_a>pi)) = phase_hopa_a(find(phase_hopa_a>pi)) -pi;
end
while length(find(phase_hopa_b>cirtific)) > 1;
    phase_hopa_b(find(phase_hopa_b>pi)) = phase_hopa_b(find(phase_hopa_b>pi)) - pi;
end
phase_diff = phase_hopa_b-phase_hopa_a;
RSS_diff = RSS_hopa_b-RSS_hopa_a;
% RSSIa = data_a(:,2);
% RSSIb = data_b(:,2);
% RSSIa_new = interp1(timea,RSSIa,time_new,"linear",'extrap');
% RSSIb_new = interp1(timeb,RSSIb,time_new,"linear",'extrap');
% RSSI_diff = RSSIb_new-RSSIa_new;
% % figure
% % subplot(2,1,1)
% % plot(phase_hopa_a,'-', LineWidth=1);
% % hold on
% % plot(phase_hopa_b,'-', LineWidth=1);
% % legend('C1','C2')
% % set(gca, 'FontSize', 18, 'Fontname', 'Arial', 'FontWeight', 'normal');
% % % xlabel('Sample Number','fontsize',22,'fontname','Arial','FontWeight','normal');
% % ylabel('Phase(rad)','fontsize',18,'fontname','Arial','FontWeight','normal');
% % 
% % subplot(2,1,2)
% % plot(phase_diff,'-', LineWidth=1);
% % set(gca, 'FontSize', 18, 'Fontname', 'Arial', 'FontWeight', 'normal');
% % xlabel('Sample Number','fontsize',18,'fontname','Arial','FontWeight','normal');
% % ylabel('Relative Phase(rad)','fontsize',18,'fontname','Arial','FontWeight','normal');

means(kk) = mean(phase_diff);
% saveppt('E:\experiment\0206\Presentation1.pptx');  
fid = fopen(['height150-' num2str(kk) '.txt'], 'a+');%' num2str(ante) '
for ii = 1:length(phase_diff)
        fprintf(fid,'%f',phase_diff(ii)); 
        fprintf(fid,'\t');
        fprintf(fid,'%f',RSS_diff(ii)); 
        % fprintf(fid,'\t');
%         % fprintf(fid,'%f',fre); 
%         % fprintf(fid,'\t');
%         % fprintf(fid,'%d',tagname); 
%         % fprintf(fid,'\t');
%         % fprintf(fid,'%d',y); 
%         % fprintf(fid,'\t');
%         % fprintf(fid,'%d',count); 
%         % fprintf(fid,'\t');
%         % fprintf(fid,'%d',second);
%         % fprintf(fid,'\t');
%         fprintf(fid,'%f',time_new(ii));
%         fprintf(fid,'\t');
        fprintf(fid,'\n');
        % fclose(fid);
end
fclose(fid);    
% plot(phase_hopa);
% hold on
% plot(phase_hopb);

% figure
% subplot(2,1,1)
% 
% plot(RSSIa_new);
% hold on
% plot(RSSIb_new);
% legend('C1','C2')
% set(gca, 'FontSize', 18, 'Fontname', 'Arial', 'FontWeight', 'normal');
% % xlabel('Sample Number','fontsize',22,'fontname','Arial','FontWeight','normal');
% ylabel('RSS(dBm)','fontsize',18,'fontname','Arial','FontWeight','normal');
% 
% 
% subplot(2,1,2)
% plot(RSSI_diff-min(RSSI_diff));
% set(gca, 'FontSize', 18, 'Fontname', 'Arial', 'FontWeight', 'normal');
% xlabel('Sample Number','fontsize',18,'fontname','Arial','FontWeight','normal');
% ylabel('Relative RSS(dBm)','fontsize',18,'fontname','Arial','FontWeight','normal');
% % saveppt('E:\experiment\0206\Presentation1.pptx'); 
end
figure
plot(means,'-*')



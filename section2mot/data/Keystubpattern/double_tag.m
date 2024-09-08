clear all
close all
clc
dis = 50
path = ['..\0831\dis(dis=1.5)\' ];
% k_tag = [3,6,7,10];
k_tag = 1:1:12;
for kk=1:length(k_tag)
a=load([path num2str(dis) '\' num2str(k_tag(kk)) '.txt']);
% a=load([path '\' num2str(k_tag(kk)) '.txt']);

tagID = unique(a(:,4));
trueID = [2215,2216];
a=a(ismember(a(:,4),trueID),:);
if length(tagID) == 2 
a(find(a(:,4) == tagID(1)),1);
data_a = a(find(a(:,4) == tagID(1)),:);
count1 = sum(a(:,4)==tagID(1));
data_b = a(find(a(:,4) == tagID(2)),:);
count2 = sum(a(:,4)==tagID(2));
% milisecond
timea = data_a(:,9);
timeb = data_b(:,9);
Timer = max(max(data_a(:,9)),max(data_b(:,9)));
time_new = union(timea,timeb);

phasea = data_a(:,1);
phaseb = data_b(:,1);

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
phase_hopb = phaseb;

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
means(kk) = mean(phase_diff);
%%%%%%%calculate_RR
read_rate1 = count1/Timer;
read_rate2 = count2/Timer;
kk
RR(kk) = min(read_rate1,read_rate2)
fid = fopen([path  num2str(dis) '-' num2str(k_tag(kk)) '.txt'], 'a+');%' num2str(ante) '
for ii = 1:length(phase_diff)
        fprintf(fid,'%f',phase_diff(ii)); 
        fprintf(fid,'\t');
        fprintf(fid,'%f',RSS_diff(ii)); 
        fprintf(fid,'\n');
end
fclose(fid);  
else
    RR(kk) = 0;
    means(kk)=0;
end
end
%%%%%%

%%%%%%
figure
plot(means,'-*')
% 
% fid = fopen([path num2str(dis) '-RR.txt'], 'a+');%' num2str(ante) '
% for ii = 1:length(RR)
%         fprintf(fid,'%f',RR(ii)); 
%         fprintf(fid,'\n');
% end
% fclose(fid); 


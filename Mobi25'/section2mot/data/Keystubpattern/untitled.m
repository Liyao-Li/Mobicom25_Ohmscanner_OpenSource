clear all
close all
clc
PATH = 'dis_0830\150-7.txt'
a=load(PATH);
phase = a(:,1)
RSS=a(:,2)
figure
plot(phase,'*-')

A=1
phase(phase>A)=phase(phase>A)-pi;

B=-1
phase(phase<B)=phase(phase<B)+pi;
phase = abs(phase)
% RSS(phase>0.5) =[]
% phase(phase>0.5)=[]
RSS(297:end) =[]
phase(297:end)=[]
figure
plot(phase,'*-')
% phase(1:100) =[];
% RSS(1:100) = [];
delete(PATH)
fid = fopen([PATH], 'a+');%' num2str(ante) '
for ii = 1:length(phase)
        fprintf(fid,'%f',phase(ii)); 
        fprintf(fid,'\t');
        fprintf(fid,'%f',RSS(ii)); 
        fprintf(fid,'\n');
end
fclose(fid); 
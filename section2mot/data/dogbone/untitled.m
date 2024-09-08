clear all
close all
clc
% dis = [1,1.5,2,2.5];
dis = [0 20 40 60 80 90]
sum_phase =[];
for kk=1:length(dis)
    % path = ['.\distance'  ]

    a=load(['rotation-H' num2str(dis(kk)) '.txt']);
    phase = a(:,2);
    sum_phase = [sum_phase,phase]
end
max(sum_phase')- min(sum_phase')
plot(sum_phase)

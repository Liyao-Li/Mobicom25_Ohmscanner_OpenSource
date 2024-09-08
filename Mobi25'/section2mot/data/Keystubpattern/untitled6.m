fid = fopen([path '/B-' num2str(kk) '.txt'], 'a+');%' num2str(ante) '
for ii = 1:length(phase_diff)
        fprintf(fid,'%f',data(ii)); 
        fprintf(fid,'\t');
        fprintf(fid,'\n');
%         fclose(fid);
end
fclose(fid);    
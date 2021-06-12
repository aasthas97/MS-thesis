function getdata2()
    for idx1 = 1 % skipped 8, 17, 20, 26, 28, 29_3, 30, 31_7, 32, 34, 36, 45, 47, 48
        for idx2 = 1
            diaryname = strcat(num2str(idx1), '_', num2str(idx2), '.txt');
            diary (diaryname)
            filename = strcat('C:\Users\aasth\Documents\Thesis_new\Data\skeletons2\', num2str(idx1), '_', num2str(idx2), 'skel.png');
            fprintf('\n%s\n', filename);
            im = imchange(filename); %convert to 105 x 105 logical
            fit_motorprograms(im, 10, true, false, true);
            automate('MP', 'bestM_pass2'); 
            diary off
        end
    end 
end

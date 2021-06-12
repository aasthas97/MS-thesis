function alldata = centredata()
    objects = {'man', 'table', 'telephone', 'umbrella'};
%     objects = {'cat', 'dog', 'eagle', 'man', 'table', 'telephone', 'umbrella'};
    for object = objects
        objectdata(object{1,1})
    end
end

function objectdata = objectdata(objectname)
    for index = 1:10
        filename = strcat('C:\Users\aasth\Downloads\', objectname, num2str(index), 'skel.png');
        im = imchange(filename);
        MP = fit_motorprograms(im, 1, true, false, true);
        MPname = strcat(objectname, num2str(index), 'MP.mat');
        save(MPname, 'MP');
        controlpoints = getcontrolpoints(MP); % extract control points from MP struct
        [angleslist, pointslist] = invtan(controlpoints); % transform control points 
        [anglecentres, pointcentres] = centres(angleslist, pointslist); % get the centre for all points and angles for each stroke
        objectdata = table(anglecentres, pointcentres);
        datafilename = strcat(objectname, num2str(index), '.xls');
        writetable(objectdata, datafilename);
    end            
end
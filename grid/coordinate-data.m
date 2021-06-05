function coord_data()
    for imnumber = 1:50
        for skelnumber = 1:10
            imfile = strcat('.\Data\imageskel\', num2str(imnumber), '_', num2str(skelnumber), 'skel.png');
            fprintf('%s', imfile);
            im = imchange(imfile);
            % define filename to store motor program
            mpfilename = strcat(num2str(imnumber), '_', num2str(skelnumber), '.png');
            mp = fit_motorprograms(im, 1, true, false, true, mpfilename);
            
            % define filename to store coordinate data in
            excelfilename = strcat('.\', num2str(imnumber), '_', num2str(skelnumber), '.xlsx');
            % extract x y coordinates from motor program and write to
            % filename
            coordinates(mp, excelfilename);
        end
    end
    
end

function coordinates(MP, filename)
% extract stroke-wise x, y coordinates from motor program 'MP' and write to
% 'filename'
    ns = MP.models{1, 1}.ns;
    for nstroke = 1:ns
       stroke = MP.models{1, 1}.motor{nstroke, 1};
       stroke_size = size(stroke);
       if stroke_size(1) > 1
           % multiple substrokes present
           trajectory = [];
           for nsubstroke = 1:stroke_size
              % do something 
              substroke = MP.models{1, 1}.motor{nstroke, 1}{nsubstroke, 1};
              trajectory = vertcat(trajectory, substroke);
           end
       else
          % only 1 substroke
          trajectory = MP.models{1, 1}.motor{nstroke, 1}{1, 1};
       end    
       
       range_idx = strcat(char(2*nstroke + 95), num2str(1));
       writematrix(trajectory, filename, 'Range', range_idx);
    end    
end

function adMat = getAdjMat()
% get adjacency matrices for image skeletons
    for imnumber = 11:30
        for skelnumber = 1:10
            imfile = strcat('C:\Users\aasth\Documents\Thesis\Data\skeletons2\', num2str(imnumber), '_', num2str(skelnumber), 'skel.png'); 
            im = imcomplement(imchange(imfile));
            % define filename to store motor program
            matFilename = sprintf('%d_%dmatrix.csv', imnumber, skelnumber);
            skel = extract_skeleton(im);
            adMat = skel.E;
            writematrix(adMat, matFilename);
        end
    end
    
end
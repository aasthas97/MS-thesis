function eiMat = getEIMat()
% get adjacency matrices for image skeletons
    for imnumber = 1:10
        for skelnumber = 1:10
            imfile = strcat('C:\Users\aasth\Documents\Thesis_new\Data\skeletons2\', num2str(imnumber), '_', num2str(skelnumber), 'skel.png'); 
            im = imcomplement(imchange(imfile));
            % define filename to store motor program
            matFilename = sprintf('%d_%deimatrix.csv', imnumber, skelnumber);
            skel = extract_skeleton(im);
            eiMat = skel.EI;
            writecell(eiMat, matFilename);

        end
    end
    
end
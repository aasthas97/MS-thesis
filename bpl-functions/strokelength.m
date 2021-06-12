function lengths = strokelength()
    for imnumber = 1:10
        for skelnumber = 1:10
            imfile = strcat('C:\Users\aasth\Documents\Thesis_new\Data\skeletons2\', num2str(imnumber), '_', num2str(skelnumber), 'skel.png'); 
            im = imcomplement(imchange(imfile));
            lenFilename = sprintf('%d_%dlengths.csv', imnumber, skelnumber);
            skel = extract_skeleton(im);
            skel_strokes = skel.S;
            sz = size(skel_strokes);
            lengths = cell(sz(1), 1);
            for i = 1:sz(1)
                xy = skel_strokes{i, 1};
                x1 = xy(1, 1);
                y1 = xy(1, 2);
                sz2 = size(xy);
                x2 = xy(sz2(1), 1);
                y2 = xy(sz2(1), 2);
                strokeLen = pdist([x1, y1; x2, y2], 'euclidean');
                lengths{i, 1} = strokeLen;
            end
            writecell(lengths, lenFilename);
        end
    end
end

        
function [im] = imchange(image_name)
    im = rgb2gray(imread(image_name));
    im = imcomplement(logical(imresize(im, [105 105])));
end
    
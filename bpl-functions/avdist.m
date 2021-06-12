function avdist = avdist(best, original)
    distances = [];
    for index = 1:size(best)
        bestX = best(index, 1);
        origX = original(index, 1);
        bestY = best(index, 2);
        origY = original(index, 2);
        dist = sqrt(((bestX - origX)^2) + ((bestY - origY)^2));
        distances = horzcat(distances, dist);
    end
    avdist = mean(distances);
end
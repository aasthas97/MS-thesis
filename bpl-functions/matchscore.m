function matchscore = matchscore(best, original)
    matchscore = 0;
    for index = 1:size(best)
        if best(index, 1) == original(index, 1) && best(index, 2) == original(index, 2)
            matchscore = matchscore + 1;
        end
    end
    fprintf('Score = %d', matchscore);
end
        
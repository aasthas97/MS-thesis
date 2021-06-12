function controlpoints = getcontrolpoints(MP)
% returns nx1 cell array, where n = # of strokes
% ith cell contains control points corresponding to the ith stroke
    ns = MP.models{1, 1}.ns;
    controlpoints = cell(ns,1);
    
    for index=1:ns
        control = MP.models{1, 1}.S{index, 1}.shapes_token;
        controlpoints{index} = control;
    end
end
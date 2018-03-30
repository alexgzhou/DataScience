function res = Normalize(x)
    maxs = max(x(:));
    mins = min(x(:));
    res = (x - mins) / (maxs - mins);
end

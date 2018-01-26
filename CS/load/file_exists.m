function [found] = file_exists(path)
    found = false;
    if exist(path, 'file') == 2
        found = true;
    end    
end
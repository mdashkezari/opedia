function [diff_right, diff_left, diff_up, diff_down]=Dispersion(X2, Y2)

%%  Comoute the separation between each tracer (one tracer at each grid point)
%%  with  respect to their own immediate neighbors (right, left, up, down))
    

    diffX_right= X2-circshift(X2,[0,1]);
    diffY_right= Y2-circshift(Y2,[0,1]);
    diff_right= (diffX_right.^2 + diffY_right.^2).^0.5;
    diff_right=diff_right(2:size(diff_right,1)-1,2:size(diff_right,2)-1);    % remove one row/column from right-left/up-down
    
    diffX_left= X2-circshift(X2,[0,-1]);
    diffY_left= Y2-circshift(Y2,[0,-1]);
    diff_left= (diffX_left.^2 + diffY_left.^2).^0.5;
    diff_left=diff_left(2:size(diff_left,1)-1,2:size(diff_left,2)-1);    % remove one row/column from right-left/up-down
    
    diffX_up= X2-circshift(X2,[-1,0]);
    diffY_up= Y2-circshift(Y2,[-1,0]);
    diff_up= (diffX_up.^2 + diffY_up.^2).^0.5;
    diff_up=diff_up(2:size(diff_up,1)-1,2:size(diff_up,2)-1);    % remove one row/column from right-left/up-down

    diffX_down= X2-circshift(X2,[1,0]);
    diffY_down= Y2-circshift(Y2,[1,0]);
    diff_down= (diffX_down.^2 + diffY_down.^2).^0.5;
    diff_down=diff_down(2:size(diff_down,1)-1,2:size(diff_down,2)-1);    % remove one row/column from right-left/up-down








%{    
    [max_separation, max_ind]= nanmax( [nanmax(nanmax(diff_right)) nanmax(nanmax(diff_left)) nanmax(nanmax(diff_up)) nanmax(nanmax(diff_down))]);
    min_separation= nanmin( [nanmin(nanmin(diff_right)) nanmin(nanmin(diff_left)) nanmin(nanmin(diff_up)) nanmin(nanmin(diff_down))]);
    disp(['      Maximum Separation: ', sprintf('%.3f',max_separation), ' [degrees]'])
    
    switch max_ind
        case 1
            delta = diff_right;            
        case 2
            delta= diff_left;
        case 3
            delta= diff_up;
        case 4
            delta= diff_down;
    end;        
    
    [max_i, max_j]= find(delta==max(max(delta)));

%}

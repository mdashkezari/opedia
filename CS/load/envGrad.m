function [delta]=envGrad(env)

    diff_right= env-circshift(env,[0,1]);
    diff_right=diff_right(2:size(diff_right,1)-1,2:size(diff_right,2)-1);    % remove one row/column from right-left/up-down

    diff_left= env-circshift(env,[0,-1]);
    diff_left=diff_left(2:size(diff_left,1)-1,2:size(diff_left,2)-1);    % remove one row/column from right-left/up-down

    diff_up= env-circshift(env,[-1,0]);
    diff_up=diff_up(2:size(diff_up,1)-1,2:size(diff_up,2)-1);    % remove one row/column from right-left/up-down

    diff_down= env-circshift(env,[1,0]);
    diff_down=diff_down(2:size(diff_down,1)-1,2:size(diff_down,2)-1);    % remove one row/column from right-left/up-down


 %   delta=(diff_right+diff_left+diff_up+diff_down)/4; 
    
    delta=(abs(diff_right)+abs(diff_left)+abs(diff_up)+abs(diff_down))/4;
    delta(isnan(delta)==1)=inf;

%    delta(find(delta==0))=NaN;

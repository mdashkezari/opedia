% Calculate Okubo-Weiss parameter W

function [W,sn,ss,vort] = Okubo_Weiss(U,V,delX,delY)

vx=(V(2:end,2:end)-V(2:end,1:end-1)) ./ delX;
uy=(U(2:end,2:end)-U(1:end-1,2:end)) ./ delY;

%vy=(V(2:end,2:end)-V(1:end-1,2:end)) ./ delY;
%ux=(U(2:end,2:end)-U(2:end,1:end-1)) ./ delX;

sn=0;
ss=0;
W=0;
%sn= ux-vy;   % normal component of strain
%ss= vx+uy;   % shear component of strain 
vort= vx-uy;    % relative voticity of the flow  

%W= sn.^2 + ss.^2 - vort.^2;   % OW parameter






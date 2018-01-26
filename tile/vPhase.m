function phase = vPhase(U,V,range)
  
  if range==2*pi
    phase = atan0_2pi(V,U);
  elseif range==pi
    phase = atan2(V,U);
  elseif range==pi/2
    phase = atan(V./U);
  else
    disp(['The third argument should be one of these values: 2*pi, pi, pi/2'])
    error
  end
  phase = 180 * phase /pi;
end


function t=atan0_2pi(y,x)
  t = Inf*x; %atan(y./x);

  con = x>0 & y>=0;
  t(con) = atan(y(con)./x(con));

  con = x==0 & y>0;
  t(con) = pi/2;

  con = x<0;
  t(con) = atan(y(con)./x(con)) + pi;

  con = x==0 & y<0;
  t(con) = 3*pi/2;

  con = x>0 & y<0;
  t(con) = atan(y(con)./x(con)) + 2*pi;

  %con = x==0 & y==0;
  %t(con) = 0;
end



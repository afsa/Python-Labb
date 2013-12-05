function brownianMotion( n, size, d, loop, delay )
%Simulate Brownian Motion
%   n - Number of particles, size - Size of the graph, d - is relative
%   delta

if nargin == 4
    delay = 0.2;
end

clf

delta = d*size;
axis([-size size -size size])
hold on

A = zeros(2, n);

for i = 1:loop
    ARND = A + randn(2, n).*delta;
    plot([A(1, :); ARND(1, :)], [A(2, :); ARND(2, :)])
    pause(delay)
    A = ARND;
end

end


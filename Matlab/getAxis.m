function [ area ] = getAxis( x , y, m )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here

if nargin == 2
    m = 0.1;
end

area = [[min(x) max(x)] + abs(peak2peak(x)).*[-1 1].*m [min(y) max(y)] + abs(peak2peak(y)).*[-1 1].*m];

end


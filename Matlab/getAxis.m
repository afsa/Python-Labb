function [ area ] = getAxis( x , y )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here

area = [[min(x) max(x)] + peak2peak(x).*[-0.1 0.1] [min(y) max(y)] + peak2peak(y).*[-0.1 0.1]];

end


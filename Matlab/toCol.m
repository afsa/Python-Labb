function [ x ] = toCol( x )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

if size(x, 1) == 1
    x = x';
end

end


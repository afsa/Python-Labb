function [ K ] = addRowOfOnes( H )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

K = [H; ones(1, size(H, 2))];

end


function [ J ] = getInnerMatrix( H )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

J = H;
J(:, 1) = []';
J(1, :) = [];
J(:, end) = []';
J(end, :) = [];

end


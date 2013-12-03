%Deklarera variabler
A = [2 1; 4 5];
B = [1 1; 2 3];
x = [7 9]';

%Skapa nya variabler med de deklarerade
C = A*B;
D = B*A;
F = A.*B;
G = B.*A;
z = A*x;
p = z'*z;
E = A'*A;
q = x'*x;

disp('A')
isVector(A)
disp('B')
isVector(B)
disp('C')
isVector(C)
disp('D')
isVector(D)
disp('E')
isVector(E)
disp('F')
isVector(F)
disp('G')
isVector(G)
disp('p')
isVector(p)
disp('q')
isVector(q)
disp('x')
isVector(x)
disp('z')
isVector(z)

disp('C = D?')
isequal(C,D)
disp('F = G?')
isequal(F,G)

disp('H = [eye(2) A; -1*B eye(2)];')
H = [eye(2) A; -1*B eye(2)]
H(:, 3)
H(2, :)
H(1, :) * H(:, 4)
%H(1, 1) = 2;
%H(2, :) = [1 2 3 4];

J = getInnerMatrix(H)

K = addRowOfOnes(H)

[[H; zeros(1, size(H, 2))] ones(size(H, 2)+1, 1)]

K(:)
K([4 9 12])

p = [1 1 2 3 5 8 13 21]'

p(2:end)-p(1:end-1)

q = [1 1 2 3 5 8 13 21]'
q.^2

x = [1 1 2 3]'
y = [5 8 13 21]'
z = x.^2 + y.^2

sum(K(:).^2)
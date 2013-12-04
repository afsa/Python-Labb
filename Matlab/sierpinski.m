function sierpinski (x, y, n)
    hold on
    if n > 0
        fill (x, y, 'b')
        m1 = (x(1) + x(2))/2;
        m2 = (x(1) + x(3))/2;
        m3 = (x(2) + x(3))/2;
        n1 = (y(1) + y(2))/2;
        n2 = (y(1) + y(3))/2;
        n3 = (y(2) + y(3))/2;
        m = [m1, m2, m3];
        nn = [n1, n2, n3];
        fill (m, nn, 'r')
        axis equal
        node_x_1 = [x(1), m1, m2];
        node_y_1 = [y(1), n1, n2];
        sierpinski(node_x_1, node_y_1, (n-1))
        node_x_2 = [x(2), m1, m3];
        node_y_2 = [y(2), n1, n3];
        sierpinski(node_x_2, node_y_2, (n-1))
        node_x_3 = [x(3), m2, m3];
        node_y_3 = [y(3), n2, n3];
        sierpinski(node_x_3, node_y_3, (n-1))
    end

function gauss_jacobi_method()
    % System of equations
    A = [10, 2, 1
         1, 5, 1
         2, 3, 10]
    b = [7; -8; 6];

    % Number of unknowns
    n = length(b);

    % Maximum number of iterations and tolerance
    maxIterations = 10;
    tolerance = 1e-6;

    % Initial guess
    x0 = zeros(n, 1)

    % Perform Gauss-Jacobi iterations
    x = x0;
    for iteration = 1:maxIterations
        xPrev = x;

        for i = 1:n
            sigma = 0;
            for j = 1:n
                if j ~= i
                    sigma = sigma + A(i, j) * xPrev(j);
                end
            end
            x(i) = (b(i) - sigma) / A(i, i);
        end


        % Check for convergence
        if norm(x - xPrev) < tolerance
            disp("Converged!");
            break;
        end
    end

    if iteration = 4
       disp(j)
    end

    % Display the result
    disp("Solution:");
    disp(x);
end

clear
clc

% Run the Gauss-Jacobi method
gauss_jacobi_method();

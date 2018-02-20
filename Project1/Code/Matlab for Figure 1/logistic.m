% Input consists of inital value x_0, parameter R, and the number of time
% steps we'd like to compute.  Output consists of a vector of x_t values
% begining with x_0 in position 1. 

function x = logistic(x_0, R, steps)
    % Do error checking on the input values. 
    % FILL IN ERROR CHECKING.  


    % Create space for the return vector y and put x_0 in the first spot. 
    x = zeros(steps + 1, 1);
    
    x(1) = x_0;
    for i=1:steps
        x(i+1) = R * x(i) * (1 - x(i));
    end

    
end

    
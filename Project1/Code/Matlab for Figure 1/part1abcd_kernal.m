function part1abcd_kernal()
    %  This program computes the
    % logistic map for two r values and slightly different x-values, 
    % demonstrating sensitive dependence on initial conditions.  It then
    % writes out the time series to for the individual maps and pairs of
    % maps to a file.  We'll use this info to measure mutual information
    % using Kernal feature of the JiDT AutoAnayzer.  
    
    % Written by Vanessa Job, February 2018.  
    
    x_val_1 = 0.999998;
    x_val_2 = 0.999999;
    a = logistic(x_val_1, 3.1, 50);
    b = logistic(x_val_2, 3.1, 50);
    c = logistic(x_val_1, 3.95, 50);
    d = logistic(x_val_2, 3.95, 50);
    x = linspace(0,50, 51);
 
    test_kernal_ab = cat(2, a, b);
    test_kernal_cd = cat(2, c,  d);
   
   
    % Write out a and b so we can compute the cross entropy with the JIDT
    % Autoanananalzer
    dlmwrite('test_kernal_a.txt', a, ' ')
    dlmwrite('test_kernal_b.txt', b, ' ')
    dlmwrite('test_kernal_ab.txt', test_kernal_ab)
    
    
    dlmwrite('test_kernal_c.txt', c, ' ')
    dlmwrite('test_kernal_d.txt', d, ' ')
    dlmwrite('test_kernal_cd.txt', test_kernal_cd)
    
  
end

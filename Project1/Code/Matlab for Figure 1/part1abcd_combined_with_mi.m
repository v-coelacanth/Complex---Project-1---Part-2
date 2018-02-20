function part1b()
    % Plot figure 1 for assignment 1, part 2.  This program plots the
    % logistic map for two r values and slightly different x-values, 
    % demonstrating sensitive dependence on initial conditions. 
    % It also saves this data so we can run it throught the JIDT
    % AutoAnalzer to compute mutual information. 
    % Written by Vanessa Job, February 2018.
    
    x_val_1 = 0.999998;
    x_val_2 = 0.999999;
    a = logistic(x_val_1, 3.1, 50);
    b = logistic(x_val_2, 3.1, 50);
    c = logistic(x_val_1, 3.95, 50);
    d = logistic(x_val_2, 3.95, 50);
    x = linspace(0,50, 51);
 
    figure
    subplot(2,1,1)
    plot(x,a, x, b)   
    xlabel('t', 'FontSize', 20)
    ylabel('x(t)', 'FontSize', 20)
    xt = get(gca, 'XTick');
    set(gca, 'FontSize', 12)
    legend( 'x_0 = 0.999998', 'x_0 = 0.999999')
    title('(a) Two time series for r = 3.1 ') 
    
    

    
    subplot(2,1,2)
    plot(x,c, x, d)
    xlabel('t', 'FontSize', 20)
    ylabel('x(t)', 'FontSize', 20)
    xt = get(gca, 'XTick');
    set(gca, 'FontSize', 12)
    legend( 'x_0 = 0.999998', 'x_0 = 0.999999')
    title('(b) Two time series for r = 3.95')
  

    
    print -depsc figure1abcd_combined
    
    % What's the cross entropy between a and b?   c and d? 
    
    
    % Round the values in a, b, c, and d to facilliate binning.  (This is
    % based on the code Melanie demonstrated in class. 
    
    aDiscrete = int64(round(a*100));
    bDiscrete = int64(round(b*100));
    cDiscrete = int64(round(c*100));
    dDiscrete = int64(round(d*100));
    testMIab = cat(2, aDiscrete, bDiscrete);
    testMIcd = cat(2, cDiscrete,  dDiscrete);
    size(testMIab)
   
    % Write out a and b so we can compute the cross entropy with the JIDT
    % Autoanananalzer
    dlmwrite('test_entropy_a.txt', aDiscrete, ' ')
    dlmwrite('test_entropy_b.txt', bDiscrete, ' ')
    dlmwrite('test_mi_ab.txt', testMIab)
    
    
    dlmwrite('test_entropy_c.txt', cDiscrete, ' ')
    dlmwrite('test_entropy_d.txt', dDiscrete, ' ')
    dlmwrite('test_mi_cd.txt', testMIcd)
    
   

end

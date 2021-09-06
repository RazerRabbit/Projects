% James Mueller
% Number Guessing Game

b = input('Would you like to play a number guessing game? Press (1) for yes or (2) for no: '); % user choice to play
if b == 2                                                                   
    disp('That''s no fun. Goodbye.');                                       % output statement for user opt-out
elseif b == 1
end
while b == 1                                                                % loop for user opt-in
    r = randi(750);                                                         % selects random integer between 1 and 750
    a = input('Guess at an integer between 1 and 750: ');                   % user prompt to guess number   
    if 1>a||a>750                                                           % reset for invalid selection
        disp('Your guess cannot be less than 1 or greater than 750. Let''s start over. ');
    elseif (1<=a&&a<=750)&&(a~=r)                                           % opens guessing loop for valid selection
        while a~=r
            if a<r&&a>=1                                                    % input statements for low guesses
                if (r-a)>=500                                               % hint for very large gaps
                    a = input('That is way too low. Try again: ');
                elseif 250<=(r-a)&&(r-a)<500                                % hint for large gaps
                    a = input('That is too low. Try again: ');
                elseif 100<=(r-a)&&(r-a)<250                                % hint for medium gaps
                    a = input('That is a little low. Try again: ');
                elseif 10<=(r-a)&&(r-a)<100                                 % hint for small gaps
                    a = input('That is close, but a little low. Try again: ');
                elseif 1<=(r-a)&&(r-a)<10                                   % hint for very small gaps
                    a = input('That is very close. Try a little higher: ');   
                else
                end
            elseif a>r&&a<=750                                              % input statements for high guesses  
                if (a-r)>=500                                               % hint for very large gaps
                    a = input('That is way too high. Try again: ');
                elseif 250<=(a-r)&&(a-r)<500                                % hint for large gaps
                    a = input('That is too high. Try again: ');
                elseif 100<=(a-r)&&(a-r)<250                                % hint for medium gaps
                    a = input('That is a little high. Try again: ');
                elseif 10<=(a-r)&&(a-r)<100                                 % hint for small gaps
                    a = input('That is close, but a little high. Try again: ');
                elseif 1<=(a-r)&&(a-r)<10                                   % hint for very small gaps
                    a = input('That is very close. Try a little lower: ');
                else
                end
            elseif 1>a||a>750                                               % input statement for invalid selections 
                a = input('Your guess cannot be less than 1 or greater than 750. Try again: ');
            end
        end
    end       
if (1<=a&&a<=750)&&(a==r)                                                   % output statement for correct guess 
        fprintf('You guessed it! The number was %g.\n', r);
        b = input('Would you like to play again? Press (1) for yes or (2) for no: '); % user choice to opt-in/out 
        if b == 2
            disp('Thanks for playing! Goodbye.');                           % output statement for user opt-out
        end
end   
end
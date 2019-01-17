message = 'hello';

for n = 1:numel(message)
    disp(strcat(['Element ',num2str(n),' is ',message(n)]))
end
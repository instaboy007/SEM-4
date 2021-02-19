function[answer]=operations()
x=input('ENTER THE FIRST OPERAND :');
y=input('ENTER THE SECOND PARAMETER :');
choice=input('1.)ADD,2.)SUBTRACT,3.)MULTIPLY,4.)DIVIDE ENTER YOUR CHOICE ==>');
if choice==1
    answer=x+y;
elseif choice==2
    answer=x-y;
elseif choice==3
    answer=x*y;
elseif choice==4
    answer=x/y;
else
    printf('ENTER VALID OPERATION !')
end
    
%   operations()
%   ENTER THE FIRST OPERAND: 
%   ENTER THE SECOND OPERAND: 
%   1.)ADD,2.)SUBTRACT,3.)MULTIPLY,4.)DIVIDE ENTER YOUR CHOICE ==>'

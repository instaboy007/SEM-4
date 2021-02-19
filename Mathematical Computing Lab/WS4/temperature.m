function temperature()
Kelvin = input('ENTER THE TEMPERATURE IN KELVIN :');
degree = Kelvin-273.15;
if degree < 32
    disp('ICE');
elseif degree < 212
    disp('WATER');
else
    disp('STEAM');
end
 
%   temperature()
%   ENTER THE TEMPERATURE IN KELVIN :

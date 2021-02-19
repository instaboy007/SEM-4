balance = 1000;
for year = 1:30
    balanceVector(year) = (1.08)*balance; 
    balance = balanceVector(year);
end
balance;
plot(1:30, balanceVector)

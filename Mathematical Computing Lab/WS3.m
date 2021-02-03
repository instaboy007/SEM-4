%1.)
    x=[1,2,3,4,5,6,7,8,9,10];
    y=[2,5,6,7,8,10,13,15,18,19];
    %plot(x,y);

%2.)
    %line(x,y,'linestyle',':','color','r','marker', 'o','markeredgecolor','g','markerfacecolor','y','linewidth',2,'markersize',12)
    
%3.)
    %x=-2:0.01:4
    %plot(x,power(3.5,(0.5.*x)).*cos(6.*x))
    
%4.)
    %x=1:0.01:10
    %plot(x,power(x,2))
    %plot(x,power(x,3))
    %plot(x,log10(x))
    %plot(x,1./x)
    
%5.)
    %x=0:0.01:2*pi
    %plot(x,sin(x))
    %plot(x,cos(x))
    %fplot(@(x)tan(x),[0,2*pi])
    
%6.)
    %clf;%clears the figure
    %fplot(@(x)power(x+5,2)./(4+3.*power(x,2)),[-3,5])
    %title ('fplot() single function');
    
%7.)
    %x=-2:0.01:4;
    %plot(x,3*x.^3 - 26*x + 10)
    %x = linspace(-2,4);
    %y = 3.*((x).^3)-26.*x+10;
    %yd = diff(y);
    %ydd = diff(yd);
    %vec_1 = x(1:end-1);
    %vec_2 = x(1:end-2);
    %plot(x,y,vec_1,yd,vec_2,ydd)
    
%8.)
    %x=-2:0.01:4;
    %plot(x,3*x.^3 - 26*x + 10)
    %x = linspace(-2,4);
    %y = 3.*((x).^3)-26.*x+10;
    %yd = diff(y);
    %ydd = diff(yd);
    %vec_1 = x(1:end-1);
    %vec_2 = x(1:end-2);
    %plot(x,y)
    %hold on
    %plot(vec_1,yd)
    %hold on
    %plot(vec_2,ydd)
    %hold off
    
%9.)
x=10:0.01:22
plot(x,95000./x.^2)
xlabel('x')
ylabel('95000/x^2')
title('95000/x^2 for x = 10:0.01:22')
text(pi, 0.7, 'arbitrary text')
legend('95000/x^2')
axis([1, 2, 3, 4], 'square')

%11
    %x=1:0.01:10;
    %plot(x,power(x,2),x,power(x,3),x,log10(x),x,1./x)

%12
    %y = @(x)(x+1)(x-2)(2*x-0.25) - exp(x);
    %subplot(2,1,1)
    %fplot(y,[0 3])
    %subplot(2,1,2)
    %fplot(y,[-3 6])
    
    
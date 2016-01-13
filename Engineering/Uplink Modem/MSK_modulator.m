#!/opt/local/bin/octave
clear all
close all

N=5;
#number of bits

bits = rand(1,N) > 0.5;
#binary 0's and 1's

#disp(bits);
##show the binary 0's and 1's

fs = 100;
#sampling rate. 1/fs is our sampling interval.

fc = 1;
#center frequency of fm carrier signal?

T = 1; 
#T is the end of the sampling interval. 

ts = [0:1/fs:T];
#Create an array of sample times.
#ts is an array from 1 to T with 1/fs steps.

#disp("ts is:");
#disp(ts);

ts = ts(1:end-1);
#Modify the ts array to remove final sample time.
#This causes it to end cleanly at one sample time before T.


tsR = kron(ones(1,N),ts);
#kron = obtain the Kronecker product of two or more matrices.
#ones(1,N) makes a 1xN matrix of all ones.
#ts is the list of sampling times which includes T at end.
#We have created a matrix where there are N ts rows.
#Each bit in bits gets a row of sampling times of its own.


math_bits = 2*bits-1; 
#converts 0's to -1 and 1's to 1

#disp(math_bits);

#generate the two frequencies corresponding to 0 and 1
# 0 is fc - 1/4T
# 1 is fc + 1/4T

fm = math_bits/(4*T);
#Divide the math_bits (the -1's and 1's) by 4*T.


#disp("fm is math_bits/(4*T):");
#disp(fm);


fmR = kron(fm,ones(1,fs));
#fm is 1 by N matrix of the frequencies associated with 0's and 1's. 
#ones(1,fs) is a 1 by fs matrix of all 1's. e.g. 100 ones.
#The Kronecker product is a 1 by fs*N matrix!
#each bit is represented by its associated frequency for fs entries.
#Matrix ends when all N bits are represented fs times each. 

#disp("fs is");
#disp(fs);
#disp("ones(1,fs) is");

#disp(ones(1,fs));
#disp("kron(fm,ones(1,fs)) is");
#disp(kron(fm,ones(1,fs)));



#generating the phase
theta = pi/2*filter([0 1],[1 -1],math_bits);

#filter(b, a, x) is
# sum from k = 0 to N of a(k+1)*y(n-k) = sum k = 0 to M of b(k+1)*x(n-k)
# for 1<=n<=length(x)
# N is length of a, minus 1. Therefore, 1 here.
# M is length of b, minus 1. Therefore, 1 here. 


# b = [0 1]
# a = [1 -1]
# x = math_bits [whatever 1s and -1s we came up with]
# for 1 <= n <= length of math_bits, which is N in our model. 
# let’s say we will only have math_bits of length 3.
# x = [1,0,1]
# By the principle of superposition, 
# the response y[n] of a discrete-time LTI system 
# is the sum of the responses to the individual 
# shifted impulses making up the input signal x[n]

# sum from k = 0 to 1 of [0 1](k+1)*y(n-k) is equal to 
# sum k = 0 to 1 of [1 -1](k+1)*x(n-k)
#
# k=0: n=0:  [0 1]*y(0)  =  [1 -1]*x(0)
# k=0: n=1:  [0 1]*y(1)  =  [1 -1]*x(1)
# k=0: n=2:  [0 1]*y(2)  =  [1 -1]*x(2)
# k=1: n=0:  [0 1]*y(-1) =  [1 -1]*x(-1)
# k=1: n=1:  [0 1]*y(0)  =  [1 -1]*x(0)
# k=1: n=2:  [0 1]*y(1)  =  [1 -1]*x(1)


thetaR = kron(theta,ones(1,fs));
#repeating?

xt = cos(2*pi*(fc+fmR).*tsR + thetaR);

#plotting here
subplot(3,1,1),plot(kron(math_bits, ones(1,fs)));
axis([0 N*fs -1.25 1.25]);grid on
subplot(3,1,2), plot(xt);
axis([0 N*fs -1 1]);grid on

subplot(3,1,3),plot(kron(mod(theta*180/pi,360),ones(1,fs)));
axis([0 N*fs -360 360]);grid on




frequency = 10;
timeperiod = 1/frequency;
amplitude = 1;
dcoffset = 0;

t = 0:0.01:2*timeperiod;
out = dcoffset+amplitude*cos(2*pi*frequency*t);

#x = -10:0.1:10;
#subplot (4,1,4), plot (x, sin (x));




















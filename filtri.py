#!/usr/bin/python3
from pylab import *
from scipy.signal import zpk2tf, dstep

filts = []
zpks = []

def genfilt(z,p,k):
    return zpk2tf(z,p,k)

theta = linspace(0, 2*pi, 1000)
circ_x = cos(theta); circ_y = sin(theta)

figure(1)
subplot(2, 6, 1)

plot_cnt = 1

def parse(z, p, k):
    b, a = zpk2tf(z,p,k)
    global plot_cnt
    subplot(2, 6, plot_cnt)
    title("Sistem " + str(plot_cnt))
    plot( real(z), imag(z), 'o')
    plot( real(p), imag(p), 'x')
    plot(circ_x, circ_y, '--')
    axis([-1.5, 1.5, -1.5, 1.5])
    axis("equal")
    grid()
    t, y = dstep( (b,a,1) )
    
    subplot(2,6,plot_cnt+6)
    plot(t, y[0])
    grid()

    plot_cnt += 1

r = sqrt(2)/2

parse(
    [1 + 0j],
    [r*exp(1j*pi/4), r*exp(-1j*pi/4)], 
    [1]
)

parse(
    [-1, -1],
    [ 0.9*exp(1j*pi/6), 0.9*exp(-1j*pi/6) ], 
    [1]
)

parse(
    [ 0.95*exp(1j*pi/11), 0.95*exp(-1j*pi/11) ],
    [ 0.90*exp(1j*pi/12), 0.90*exp(-1j*pi/12) ], 
    [1]
)

parse(
    [ -1, -1 ],
    [ r*exp(1j*pi/6), r*exp(-1j*pi/6) ], 
    [1]
)

parse(
    [ -1, +1 ],
    [ 0.9*exp(1j*pi/12), 0.9*exp(-1j*pi/12) ], 
    [1]
)

parse(
    [ 1, 1 ],
    [ 0.9*exp(1j*pi/4), 0.9*exp(-1j*pi/4) ], 
    [1]
)


show()

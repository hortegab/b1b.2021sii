import numpy
def nyq(Sps, ntaps):
    n=numpy.linspace(int(-ntaps/2), int(ntaps/2-1), ntaps)
    h=numpy.sinc(n/Sps)
    return h

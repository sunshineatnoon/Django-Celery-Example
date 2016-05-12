from celery import shared_task
from numpy import random
from scipy.fftpack import fft

@shared_task
def fft_random(n):
    """
    Brainless number crunching just to have a substantial task:
    """
    for i in range(n):
        x = random.normal(0, 0.1, 2000)
        y = fft(x)
    return

@shared_task
def add(x,y):
    for i in range(1000000000):
        a = x+y
    return x+y

import logging
from time import time
import multiprocessing

def factorize_one_process(*numbers):
    logging.basicConfig(level=logging.DEBUG)
    timer = time()
    result = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    logging.debug(f'Solo done in {time() - timer}')
    return result

def factorize_single(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    logging.basicConfig(level=logging.DEBUG)
    timer = time()
    num_processes = multiprocessing.cpu_count()
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        result = pool.map(factorize_single, numbers)
    logging.debug(f'8 cores done in {time() - timer}')
    
    return result

if __name__ == '__main__':
    a, b, c, d = factorize_one_process(128, 255, 99999, 10651060)
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
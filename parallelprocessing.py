import multiprocessing as mp


def square(x):
    print(x * x)
    return x * x


if __name__ == '__main__':
    print("Number of processors:", mp.cpu_count())
    pool = mp.Pool(mp.cpu_count())
    inputs = [0, 1, 2, 3, 4]
    outputs_async = pool.map(square, inputs)
    # outputs = outputs_async.get()
    # print("Output: {}".format(outputs))

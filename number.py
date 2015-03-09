def test(n, a, b):

    queue = [0]

    for _ in xrange(n - 1):
        new_queue = []
        for el in queue:
            new_queue.append(el + a)
            new_queue.append(el + b)
        queue = set(new_queue)

    print queue

test(3, 1, 2)

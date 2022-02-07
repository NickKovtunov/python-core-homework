from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        import time
        def decoratedFunc(*args, **kwargs):
            commonTime = 0
            for i in range(num):
                startTime = time.time()
                func(*args, **kwargs)
                endTime = time.time()
                funcTime = endTime - startTime
                number = i + 1
                print("Прогон " + str(number) + ": " + str(funcTime))
                commonTime = commonTime + funcTime

            result = commonTime / num
            print("Среднее время: " + str(result))
        return decoratedFunc
        pass
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)

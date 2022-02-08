from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):

        def decorated_func(*args, **kwargs):
            common_time = 0
            for i in range(num):
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                func_time = end_time - start_time
                number = i + 1
                print("Прогон " + str(number) + ": " + str(func_time))
                common_time = common_time + func_time

            result = common_time / num
            print("Среднее время: " + str(result))
        return decorated_func
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)

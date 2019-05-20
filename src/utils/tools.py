import time

def deep_extend(*args):
    """
    A method used to extend dictionary.
    :param args: one or multiple dictionary.
    :return: updated dictionary.
    """
    result = None
    for arg in args:
        if isinstance(arg, dict):
            if not isinstance(result, dict):
                result = {}
            for key in arg:
                result[key] = deep_extend(result[key] if key in result else None, arg[key])
        else:
            result = arg

    return result


def timer(f):
    """
    A method used as decorator for timing the function
    :param f: no parameters, use as a decorator.
    :return: will print runtime time usage and function name in the console 
    """
    def wrapper(*args):
        print ('<function name: {0}>'.format(f.__name__))
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('[timecosts: {0} ms]'.format((time2-time1)*1000.0))
        return ret
    return wrapper


def retry(attempt, interval=None):
    """
    Use as a decorator. will retry the method if some error occors.
    :param attempt: attempt times
    :param interval:  retry time interval, sec.
    :return: No return use as decorator.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            att = 0
            while att < attempt:
                try:
                    return func(*args, **kwargs)
                except IOError:
                    return
                except Exception as e:
                    print(e)
                    att += 1
                    if interval:
                        time.sleep(interval)
        return wrapper
    return decorator
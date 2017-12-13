from retrying import *

@retry
def never_give_up_never_surrender():
    print("Retry forever ignoring Exceptions, don't wait between retries")

@retry(stop_max_attempt_number=7)
def stop_after_7_attempts():
    print("Stopping after 7 attempts")

@retry(stop_max_delay=10000)
def stop_after_10_s():
    print("Stopping after 10 seconds")

@retry(wait_fixed=2000)
def wait_2_s():
    print("Wait 2 second between retries")

@retry(wait_random_min=1000, wait_random_max=2000)
def wait_random_1_to_2_s():
    print("Randomly wait 1 to 2 seconds between retries")

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def wait_exponential_1000():
    print("Wait 2^x * 1000 milliseconds between each retry, up to 10 seconds, then 10 seconds afterwards")
    #2 4 8 10 10 10 10....

#We have a few options for dealing with retries that raise specific or general exceptions, as in the cases here.
def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)
@retry(retry_on_exception=retry_if_io_error)
def might_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
@retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
def only_raise_retry_error_when_not_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors wrapped in RetryError")

def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return result is None
@retry(retry_on_result=retry_if_result_none)
def might_return_none():
    print("Retry forever ignoring Exceptions with no wait if return value is None")
'''
    r = random.randint(0, 10)
    print(r)
    if r > -1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"
'''
never_give_up_never_surrender()
stop_after_7_attempts()
stop_after_10_s()
wait_2_s()
wait_random_1_to_2_s()
wait_exponential_1000()
might_io_error()
only_raise_retry_error_when_not_io_error()
might_return_none()
"""
import random
from retrying import retry

print('x')
@retry
def do_something_unreliable():
    r = random.randint(0, 10)
    print(r)
    if r > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"
print('y')
print(do_something_unreliable())
"""
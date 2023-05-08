import logging
from datetime import datetime
import sys
import time

formater = logging.Formatter("%(levelname)s: %(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formater)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

log_functions = {
    logging.DEBUG: logging.debug,
    logging.INFO: logging.info,
    logging.WARNING: logging.warning,
    logging.ERROR: logging.error,
    logging.CRITICAL: logging.critical
}

def log(level):
    def decorator(func_or_class):
        def wrapper(*args, **kwargs):
            start_date = datetime.now()
            start_time = time.perf_counter()
            # if func_or_class was func, the result is some value,
            # if it was class, we call constructor, the result is new instance
            return_val = func_or_class(*args, **kwargs)        
            duration = time.perf_counter() - start_time
            
            if isinstance(func_or_class, type):
                log_functions[level](f"Class created. Time: {start_date.strftime('%d/%m/%Y %H:%M:%S')}; " 
                                     f"Class name: {func_or_class.__name__}")
            else:
                log_functions[level](f"Function call. Time: {start_date.strftime('%d/%m/%Y %H:%M:%S')}; "
                                     f"Duration: {duration:.6f}; "
                                     f"Function name: {func_or_class.__name__}; "
                                     f"Args: {args}; "
                                     f"Kwargs: {kwargs}; "
                                     f"Return value: {return_val}")
                
            return return_val
        return wrapper
    return decorator      

@log(logging.WARNING)
def foo(x,y):
    time.sleep(2)
    return x+y

@log(logging.DEBUG)
def debug_level():
    print("This function has log level of debug so no log")

@log(logging.ERROR)
class Foo:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def doesnt_log(self):
        print("Foo method called. No log.")
        
if __name__ == '__main__':
    foo(1, y=2)
    debug_level()
    
    f = Foo(1,2)
    f.doesnt_log()
        
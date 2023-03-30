from os import environ
import sys

def contains_arg(env):
    for arg in sys.argv:
        if arg in env:
            return True
    return False

def print_env(env):
    print(f"{env} = {environ[env]}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for env in sorted(environ):
            if contains_arg(env):
                print_env(env)
    else:
        for env in sorted(environ):
            print_env(env)
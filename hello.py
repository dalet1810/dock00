import os, time

def hello():
    print(time.ctime(), 'hello from alpine python (with listdir)')
    d0 = os.listdir('.')
    print(os.getcwd(), ':', d0)

if __name__ == '__main__':
    hello()


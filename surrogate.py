import sys
import surrogate
if __name__ == "__main__":
    m = __import__ ("surrogate_"+sys.argv[1])
    func = getattr(m, sys.argv[2])
    func()

# # 19.10.1
# import time
# from timeit import timeit

# def snooze():
#     time.sleep(1)

# seconds = timeit('snooze()', globals=globals(), number=1)
# print(f"{seconds:.4f}")


# def time_decorator(func):
#     def inner(*args, **kwargs):
#         t1 = time.time()
#         result = func(*args, **kwargs)
#         t2 = time.time()
#         print(f"{(t2 - t1):.4f}")
#         return result
#     return inner

# @time_decorator
# def naptime():
#     snooze()

# naptime()


# class TimeContextManager:
#     def __enter__(self):
#         self.t1 = time.time()
#         return self
#     def __exit__(self, type, value, traceback):
#         t2 = time.time()
#         print(f"{(t2 - self.t1):.4f}")

# with TimeContextManager():
#     snooze()


# # 19.10.5 Numba
# import math
# from timeit import timeit
# from numba import jit

# def hypot(a, b):
#     return math.sqrt(a ** 2 + b ** 2)

# print(timeit('hypot(5, 6)', globals=globals()))
# print(timeit('hypot(5, 6)', globals=globals()))

# @jit
# def hypot_jit(a, b):
#     return math.sqrt(a ** 2 + b ** 2)

# print(timeit('hypot_jit(5, 6)', globals=globals()))
# print(timeit('hypot_jit(5, 6)', globals=globals()))

# @jit(nopython=True)
# def hypot_jit_nopy(a, b):
#     return math.sqrt(a ** 2 + b ** 2)

# print(timeit('hypot_jit_nopy(5, 6)', globals=globals()))
# print(timeit('hypot_jit_nopy(5, 6)', globals=globals()))

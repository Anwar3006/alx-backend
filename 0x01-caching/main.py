# import sys

# def fib(num):
#     if num == 0 or num == 1:
#         return 1
    
#     return fib(num - 1) + fib(num - 2)

# end = int(sys.argv[1])
# start = end - end
# print(f"Starting the Sequence from {start} to {end}")

# for x in range(start, end + 1):
#     num = fib(x)
#     print(num)

LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
# print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
# my_cache.put("G", "San Francisco")

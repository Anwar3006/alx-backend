#!/usr/bin/env python3
"""
Main file
"""
# Server = __import__('1-simple_pagination').Server

# server = Server()


# # print(server.get_page(1, 3))
# print('--------------------')
# print(server.get_page(3, 2))
# print(server.get_page(3000, 100))



Server = __import__('2-hypermedia_pagination').Server

server = Server()

# print(server.get_hyper(1, 2))
# print("---")
# print(server.get_hyper(2, 2))
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))
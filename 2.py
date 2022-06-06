# # # # import sys
# # # # global arr
# # # # sys.setrecursionlimit(101)
# # # arr = []
# # #
# # # # def potomok(name):
# # # #     if name != -1 and name != first:
# # # #         arr.append(name+1)
# # # #         return potomok(predok[name])
# # # #     elif name == first:
# # # #         arr.append(name+1)
# # # #         return arr
# # # #     else:
# # # #         return -1
# # #
# # #
# # #
# # #
# # # from collections import defaultdict
# # # from collections import deque
# # #
# # # n = int(input())
# # # graph = [[int(i) for i in input().split()] for j in range(n)]
# # # vertexes = defaultdict(list)
# # # # for i in range(n):
# # # #     arcs = [int(i) for i in input().split()]
# # # #     for j in range(i+1,n):
# # # #         if arcs[j] == 1:
# # # #             vertexes[i].append(j)
# # # #             vertexes[j].append(i)
# # # first,second = map(int,input().split())
# # # first -= 1; second -= 1
# # # used = [0]*n
# # # used[first] = 1
# # # levels = [n]*n
# # # levels[first] = 0
# # # predok = [-1]*n
# # # predok[first] = -1
# # # queue = deque()
# # # queue.append(first)
# # #
# # # for i in range(n):
# # #     for j in range(i+1,n):
# # #         if graph[i][j] == 1:
# # #             vertexes[i].append(j)
# # #             vertexes[j].append(i)
# # #
# # #
# # # while queue:
# # #     element = queue.popleft()
# # #     for elem in vertexes[element]:
# # #         if used[elem] != 1:
# # #             used[elem] = 1
# # #             queue.append(elem)
# # #             levels[elem] = levels[element] + 1
# # #             predok[elem] = element
# # #
# # #
# # #
# # # print(levels[second])
# # # if levels[second] != 0:
# # #     if levels[second] == n:
# # #         print(-1)
# # #     else:
# # #         while second != -1:
# # #             arr.append(second+1)
# # #             second = predok[second]
# # #         print(*reversed(arr))
# #
# # arr = []
# #
# #
# #
# # from collections import defaultdict
# # from collections import deque
# #
# # n = int(input())
# # graph = [[int(i) for i in input().split()] for j in range(n)]
# # vertexes = defaultdict(list)
# #
# # first,second = map(int,input().split())
# # first -= 1; second -= 1
# # used = [0]*n
# # used[first] = 1
# # levels = [n]*n
# # levels[first] = 0
# # predok = [-1]*n
# # queue = deque()
# # queue.append(first)
# #
# # for i in range(n):
# #     for j in range(i+1,n):
# #         if graph[i][j] == 1:
# #             vertexes[i].append(j)
# #             vertexes[j].append(i)
# #
# #
# # while queue:
# #     element = queue.popleft()
# #     for elem in vertexes[element]:
# #         if levels[elem] > levels[element] + 1:
# #             used[elem] = 1
# #             queue.append(elem)
# #             levels[elem] = levels[element] + 1
# #             predok[elem] = element
# #
# #
# #
# # print(levels[second])
# # if levels[second] != 0:
# #     if levels[second] == n:
# #         print(-1)
# #     else:
# #         while second != -1:
# #             arr.append(second+1)
# #             second = predok[second]
# #         print(*reversed(arr))
#
#
# # arr = []
# #
# #
# #
# # from collections import defaultdict
# # from collections import deque
# #
# # n = int(input())
# # graph = [[int(i) for i in input().split()] for j in range(n)]
# # vertexes = defaultdict(list)
# #
# # first,second = map(int,input().split())
# # first -= 1; second -= 1
# # levels = [n]*n
# # levels[first] = 0
# # predok = [-1]*n
# # queue = deque()
# # queue.append(first)
# #
# # for i in range(n):
# #     for j in range(i+1,n):
# #         if graph[i][j] == 1:
# #             vertexes[i].append(j)
# #             vertexes[j].append(i)
# #
# #
# # while queue:
# #     element = queue.popleft()
# #     for elem in vertexes[element]:
# #         if levels[elem] > levels[element] + 1:
# #             queue.append(elem)
# #             levels[elem] = levels[element] + 1
# #             predok[elem] = element
# #
# #
# #
# #
# # if levels[second] == n:
# # 	print(-1)
# # elif levels[second] == 0:
# # 	print(levels[second])
# # else:
# # 	while second != -1:
# # 		arr.append(second+1)
# # 		second = predok[second]
# # 	print(*reversed(arr))
#
# arr = []
#
#
#
# from collections import defaultdict
# from collections import deque
#
# n = int(input())
# graph = [[int(i) for i in input().split()] for j in range(n)]
# vertexes = defaultdict(list)
#
# first,second = map(int,input().split())
# first -= 1; second -= 1
# levels = [n]*n
# levels[first] = 0
# predok = [-1]*n
# queue = deque()
# queue.append(first)
#
# for i in range(n):
#     for j in range(i+1,n):
#         if graph[i][j] == 1:
#             vertexes[i].append(j)
#             vertexes[j].append(i)
#
#
# while queue:
#     element = queue.popleft()
#     for elem in vertexes[element]:
#         if levels[elem] > levels[element] + 1:
#             queue.append(elem)
#             levels[elem] = levels[element] + 1
#             predok[elem] = element
#
#
#
#
#
# print(levels[second])
# if levels[second] != 0:
#     if levels[second] == n:
#         print('-1')
#     else:
#         while second != -1:
#             arr.append(second+1)
#             second = predok[second]
#         print(*reversed(arr))
#
# if levels[second] == n:
#         print('-1')
#     else:
#         while second != -1:
#             arr.append(second+1)
#             second = predok[second]
#         print(*reversed(arr))


arr = []



from collections import defaultdict
from collections import deque

n = int(input())
graph = [[int(i) for i in input().split()] for j in range(n)]
vertexes = defaultdict(list)

first,second = map(int,input().split())
first -= 1; second -= 1
used = [0]*n
used[first] = 1
levels = [-1]*n
levels[first] = 0
predok = [-1]*n
queue = deque()
queue.append(first)

for i in range(n):
    for j in range(i+1,n):
        if graph[i][j] == 1:
            vertexes[i].append(j)
            vertexes[j].append(i)


while queue:
    element = queue.popleft()
    for elem in vertexes[element]:
        if used[elem] != 1:
            used[elem] = 1
            queue.append(elem)
            levels[elem] = levels[element] + 1
            predok[elem] = element





print(levels[second])
if levels[second] > 0:
    while second != -1:
        arr.append(second+1)
        second = predok[second]
    print(*reversed(arr))

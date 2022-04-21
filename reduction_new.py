# k coloring input
V = int(input())  # number of vertices 0 ≤ V ≤ 300
E = int(input())  # number of edges 0 ≤ E ≤ 25000
m = int(input())  # target number of colors 0 ≤ m ≤ 2^30
e = []  # endpoints of edges
for i in range(E):
    e.append(input().split())


def make_adjacency_list(V, E, e):
    # write code
    adj_list = ""
    return adj_list


adjacency_list = make_adjacency_list(V, E, e)


def solve_coloring(adjacency_list, V, E, m):
    adj_list = adjacency_list
    c1 = ""  # constraint 1, who can play each role
    c2 = ""  # constraint 2, which actors play in same scene
    n = V  # number of roles ≥ 2
    s = E  # wer set each edge as a scene
    k = m  # number of actors same as target colors

    return_string = str(n) + "\n" + str(s) + "\n" + str(k) + "\n" + str(c1) + "\n" + str(c2)
    return return_string


print(solve_coloring(adjacency_list, V, E, m))

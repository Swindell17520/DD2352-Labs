# k coloring input
V = int(input())  # number of vertices 0 ≤ V ≤ 300
E = int(input())  # number of edges 0 ≤ E ≤ 25000
m = int(input())  # target number of colors 0 ≤ m ≤ 2^30
e = []  # endpoints of edges
for i in range(E):
    e.append(input().split())


def solve_coloring(V, E, m):

    c1 = "1 1\n1 2\n"  # constraint 1, who can play each role
    c2 = "2 1 3\n2 2 3\n"  # constraint 2, which actors play in same scene
    n = V + 3  # number of roles ≥ 2
    s = E + 2  # we set each edge as a scene
    k = m + 3  # number of actors

    # constraint 1
    actor_string = str(m)
    for i in range(3, k + 1):
        actor_string += " " + str(i)  # add each role so a row looks like "3 1 2 3" if k = 3
    for i in range(n-2):
        c1 += actor_string + "\n"  # add a row with the actor string for each role (n roles = # vertices)
    c1 = c1.rstrip()

    # constraint 2
    for i in e:  # we make every edge as a scene
        c2 += "2 " + str(int(i[0])+2) + " " + str(int(i[1])+2) + "\n"
    c2 = c2.strip()

    return_string = str(n) + "\n" + str(s) + "\n" + str(k) + "\n" + str(c1) + "\n" + str(c2)
    return return_string


print(solve_coloring(V, E, m))

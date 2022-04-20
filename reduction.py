# k coloring input
V = int(input())  # number of vertices 0 ≤ V ≤ 300
E = int(input())  # number of edges 0 ≤ E ≤ 25000
m = int(input())  # target number of colors 0 ≤ m ≤ 2^30
e = []  # endpoints of edges
for i in range(E):
    e.append(input().split())

# how do we check if we get any isolated edges in the coloring problem????


def solve_coloring(V, E, m, e):
    c1 = ""  # constraint 1, who can play each role
    c2 = ""  # constraint 2, which actors play in same scene
    n = V  # number of roles ≥ 2
    s = E  # wer set each edge as a scene
    k = m  # number of actors same as target colors

    # CASE 1 - simplest positive casting instance has at least 3 vertices and two edges
    if V >= 3 and E >= 2: # convert the graph coloring instance to same format as casting problem
        # constraint 1, we allow all actors to play all roles
        actor_string = str(k)  # k corresponds to the number of actors which can play the certain role.
        for i in range(1, k+1):
            actor_string += " " + str(i)  # add each role so a row looks like "3 1 2 3" if k = 3
        for i in range(n):
            c1 += actor_string + "\n"  # add a row with the actor string for each role (n roles = # vertices)
        c1 = c1.rstrip()
        # constraint 2
        for v in e:  # we make every edge as a scene
            c2 += "2 " + str(v[0] + " " + str(v[1])) + "\n"

    # CASE 2 - 1 edge and at least two vertices
    elif E == 1 and V == 2:
        n += 1
        s += 1
        c1 = "3 1 2 3\n3 1 2 3\n3 1 2 3"
        for v in e:
            c2 += "3 " + str(v[0] + " " + str(v[1]) + " " + str(n))

    elif E == 1 and V > 2:
        # isolated vertices need to be handled
        raise KeyError("ops")

    # CASE 3 - only isolated vertices (positive!
    elif E == 0:
        if V != 0 and m == 0:  # negative
            n = 3
            s = 2
            k = 2  # this makes casting negative
            c1 = "2 1 2\n2 1 2"
            c2 = "2 1 3\n2 2 3"
        else:  # this is positive in coloring, we create a positive casting instance below
            n = 3
            s = 2
            k = 3
            c1 = "3 1 2 3\n3 1 2 3\n3 1 2 3"  # each role can be played by all actors
            c2 = "2 1 3\n2 2 3"  # role 1 and 3 in one scene and role 2 and 3 in the other

    # print new instance
    print(n)
    print(s)
    print(k)
    print(c1)
    print(c2)


solve_coloring(V, E, m, e)

# k coloring input
V = int(input())  # number of vertices 0 ≤ V ≤ 300
E = int(input())  # number of edges 0 ≤ E ≤ 25000
m = int(input())  # target number of colors 0 ≤ m ≤ 2^30
e = []  # endpoints of edges
for i in range(E):
    e.append(input().split())


def solve_coloring(V, E, m, e):
    n = V + 4  # 3 roles for fixing diva condition, 1 role for fixing isolated edges
    s = E + 2  # two edges for diva condition fix needed
    k = m + 4  # actors for the 4 roles

    # constraint 1 - who can play role i
    c1 = "3 1 2 3\n3 1 2 3\n3 1 2 3\n"  # role 1, 2, 3 can be played by 1, 2, 3. (diva condition fix)
    if n > 4:  # role 4 to n-1 can be played by actors 4 to n-1 (role n is for fixing isolated edges, see below)
        if k > 4:  # could be positive instance
            c1_str = str(k - 4)  # cannot be played by 1, 2, 3 or n
            for i in range(4, k):
                c1_str += " " + str(i)  # add each role so a row looks like "4 4 5 6 7" if k = 8
            for i in range(4, n):
                c1 += c1_str + "\n"
        else:  # not enough actors for the roles, this should be a negative instance
            for i in range(4, n):
                c1 += "3 1 2 3\n"  # the only actors available are 1 2 3, so we assign the roles these actors
    # now, last role n is assigned actor k (this one for fixing possible isolated vertices)
    c1 += "1 " + str(k)

    # constraint 2 - who plays in which scene
    c2 = "2 1 3\n2 2 3\n"  # diva condition fix
    for i in e:  # every edge in is made into a scene
        c2 += "2 " + str(int(i[0])+3) + " " + str(int(i[1])+3) + "\n"  # shift index so divas are not bothered
    for i in range(1, n):  # fix possible isolated vertices, with help of the extra added role/actor
        # (this role is role n (acted by actor k). we create a scene with role n and every other role)
        c2 += "2 " + str(i) + " " + str(n) + "\n"
        s += 1
    c2 = c2.rstrip()  # removing last newline

    return_string = str(n) + "\n" + str(s) + "\n" + str(k) + "\n" + str(c1) + "\n" + str(c2)
    return return_string


print(solve_coloring(V, E, m, e))


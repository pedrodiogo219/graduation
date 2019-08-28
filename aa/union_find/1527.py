import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
  sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


class Union_Find:

    def __init__(this, n, points):
        this.parent = [i for i in range(0, n)]
        this.points = points

    def printa(this):
        print(this.parent)

    def find(this, n):
        root = n
        while root != this.parent[root]:
            root = this.parent[root]

        while n != root:
            next = this.parent[n]
            this.parent[n] = root
            n = next

        return root

    def union(this, a, b):
        root_a = this.find(a)
        root_b = this.find(b)

        if root_a == root_b: return

        if root_a > root_b:
            root_a, root_b = root_b, root_a

        this.parent[root_b] = root_a
        this.points[root_a] += this.points[root_b]



def main():
    while True:
        n, m = list(map(int, input().split()))
        if n == 0 and m == 0:
            return

        points = list(map(int, input().split()))

        my_union = Union_Find(n, points)
        wins = 0
        while m > 0:
            m-=1
            option, a, b = list(map(int, input().split()))

            if option == 1:
                my_union.union(a-1, b-1)
            if option == 2:
                guild_a = my_union.find(a-1)
                guild_b = my_union.find(b-1)
                my_guild = my_union.find(0)

                if my_guild == guild_a and my_union.points[guild_a] > my_union.points[guild_b] :
                    wins+=1
                if my_guild == guild_b and my_union.points[guild_b] > my_union.points[guild_a] :
                    wins+=1

        print(wins)



main()

def generateParenthesis(self, n: int) -> List[str]:
    combination = []

    def bt(p, l, r):
        if n == r:
            combination.append(p)
        else:
            if l < n:
                bt(p + '(', l + 1, r)

            if r < l:
                bt(p + ')', l, r + 1)

    bt('', 0, 0)

    return combination

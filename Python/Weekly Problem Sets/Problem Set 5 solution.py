"""Problem Set 5 — Recursion & HTTP / APIs"""


# ── Problem 1 ─────────────────────────────────────────────────────────────────
def recursive_squares(num: int) -> list[int]:
    # base cases
    if num == 0:
        return []
    if num == 1:
        return [1]

    square = num ** 2
    result = [square]
    # recursive step
    childs_list = recursive_squares(num - 1)
    result.extend(childs_list)

    return result
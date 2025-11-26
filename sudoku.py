def solve_sudoku_fast(board):
    # 비트마스크: 1<<d (d=0..8)이면 숫자 d+1 사용 표시
    FULL = (1 << 9) - 1  # 0b111111111
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    def box_id(r, c):
        return (r // 3) * 3 + (c // 3)

    empties = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == 0:
                empties.append((r, c))
            else:
                bit = 1 << (v - 1)
                b = box_id(r, c)
                # 초기 유효성 체크
                if (rows[r] & bit) or (cols[c] & bit) or (boxes[b] & bit):
                    return False
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

    def candidates_mask(r, c):
        b = box_id(r, c)
        used = rows[r] | cols[c] | boxes[b]
        return FULL & ~used  # 사용 가능한 숫자 비트

    def backtrack():
        if not empties:
            return True

        # MRV 선택
        best_i = -1
        best_mask = 0
        best_count = 10
        for i, (r, c) in enumerate(empties):
            mask = candidates_mask(r, c)
            if mask == 0:
                return False
            cnt = mask.bit_count()
            if cnt < best_count:
                best_count = cnt
                best_mask = mask
                best_i = i
                if cnt == 1:
                    break

        r, c = empties.pop(best_i)
        b = box_id(r, c)
        mask = best_mask

        # mask에 켜진 비트들을 하나씩 꺼내며 시도
        while mask:
            bit = mask & -mask
            mask -= bit
            v = (bit.bit_length() - 1) + 1  # 비트 -> 숫자(1..9)

            board[r][c] = v
            rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit

            if backtrack():
                return True

            rows[r] &= ~bit; cols[c] &= ~bit; boxes[b] &= ~bit
            board[r][c] = 0

        empties.insert(best_i, (r, c))
        return False

    return backtrack()

# 사용 예시
if __name__ == "__main__":
    puzzle = [
        [0,9,0, 0,0,0, 0,0,2],
        [0,0,0, 0,0,0, 8,0,4],
        [0,0,0, 7,5,2, 0,0,0],
        [0,0,0, 0,9,0, 0,0,0],
        [0,4,8, 0,6,0, 0,0,7],
        [6,0,2, 0,0,5, 0,8,0],
        [0,6,0, 0,3,8, 0,7,1],
        [0,0,0, 6,0,0, 0,0,0],
        [2,0,1, 0,0,0, 0,0,0],
    ]
    if solve_sudoku_fast(puzzle):
        for row in puzzle:
            print(row)

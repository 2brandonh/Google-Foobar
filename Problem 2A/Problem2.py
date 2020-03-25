import math

def solution(start, end):
    R = 8  # board size
    C = 8
    r = int(start / R)  # row and col respectively
    c = start % C
    r_target = int(end / R)
    c_target = end % C

    if r == r_target and c == c_target:
        return 1

    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]
    # movement options

    queue = [[r, c]]
    visited = [[False for i in range(R)] for j in range(C)]
    visited[r][c] = True

    move_count = 1
    nodes_left_in_layer = 1
    nodes_left_in_next_layer = 0

    while len(queue) > 0:
        for i in range(8):
            rr = r + dx[i]  # rr and cc are new positions
            cc = c + dy[i]

            # Skip invalid coords
            if rr < 0 or cc < 0: continue
            if rr >= R or cc >= C: continue
            if visited[rr][cc]: continue

            if rr == r_target and cc == c_target:
                return move_count

            visited[rr][cc] = True
            queue.append([rr, cc])
            nodes_left_in_next_layer += 1

        queue.pop(0)
        r = queue[0][0]
        c = queue[0][1]
        nodes_left_in_layer -= 1

        if nodes_left_in_layer == 0:
            move_count += 1
            nodes_left_in_layer = nodes_left_in_next_layer
            nodes_left_in_next_layer = 0



def main():
  print(solution(7, 7))


if __name__ == "__main__":
    main()

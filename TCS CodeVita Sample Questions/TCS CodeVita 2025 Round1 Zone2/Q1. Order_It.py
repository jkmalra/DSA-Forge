from collections import deque

def order_it():
    n = int(input().strip())
    input()
    
    shuffled = []
    for i in range(n):
        shuffled.append(input().strip())
    input()

    original = []
    for i in range(n):
        original.append(input().strip())

    if shuffled == original:
        print(0)
        return

    q = deque()
    seen = set()

    q.append((tuple(shuffled), 0))
    seen.add(tuple(shuffled))

    while q:
        current, steps = q.popleft()
        if list(current) == original:
            print(steps)
            return

        for i in range(n):
            for j in range(i + 1, n + 1):
                cut = current[i:j]
                remaining = current[:i] + current[j:]

                for k in range(len(remaining) + 1):
                    new_state = remaining[:k] + cut + remaining[k:]
                    if new_state not in seen:
                        seen.add(new_state)
                        q.append((new_state, steps + 1))

if __name__ == "__main__":
    order_it()
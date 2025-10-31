def play_game():
    n = int(input())
    p1 = []
    p2 = []

    def get_value(card):
        if card == 'A':
            return 1
        elif card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        else:
            return int(card)

    for i in range(n):
        c1, s1, c2, s2 = input().split()
        p1.append((get_value(c1), int(s1)))
        p2.append((get_value(c2), int(s2)))

    suit_order = list(map(int, input().split()))
    suit_rank = {}
    for i in range(len(suit_order)):
        suit_rank[suit_order[i]] = i

    def sort_cards(cards):
        return sorted(cards, key=lambda x: (x[0], suit_rank[x[1]]))

    from collections import deque
    q1 = deque(p1)
    q2 = deque(p2)
    table = []
    turn_p1 = True

    def can_beat(new_card, last_card):
        if new_card[0] == last_card[0]:
            return suit_rank[new_card[1]] < suit_rank[last_card[1]]
        return False

    while q1 and q2:
        if turn_p1:
            card = q1.popleft()
        else:
            card = q2.popleft()

        if len(table) == 0:
            table.append(card)
            turn_p1 = not turn_p1
        else:
            top = table[-1]
            if can_beat(card, top):
                table.append(card)
                sorted_table = sort_cards(table)
                table.clear()

                if turn_p1:
                    q1.extend(sorted_table)
                else:
                    q2.extend(sorted_table)
            else:
                table.append(card)
                turn_p1 = not turn_p1

    if len(q1) > 0 and len(q2) == 0:
        print("WINNER")
    elif len(q2) > 0 and len(q1) == 0:
        print("LOSER")
    else:
        print("TIE")


if __name__ == "__main__":
    play_game()
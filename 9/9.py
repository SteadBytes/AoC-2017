from collections import deque


def solution(char_queue):
    current_score = total_score = non_cancelled = 0
    score_stack = []
    garbage = False

    while char_queue:
        ch = char_queue.popleft()
        if ch == '!':
            ch = char_queue.popleft()
        elif garbage:
            if ch == '>':
                garbage = False
            else:
                non_cancelled += 1
        elif ch == '{':
            current_score += 1
            score_stack.append(current_score)
        elif ch == '<':
            garbage = True
        elif ch == '}':
            current_score -= 1
            total_score += score_stack.pop()
    return total_score, non_cancelled


if __name__ == '__main__':
    stream = deque()
    with open('input.txt') as f:
        # map each character to own element in queue
        stream = deque(map(lambda x: x, f.readlines()[0]))
    total_score, non_cancelled = solution(stream)
    print('Total Score: %s' % total_score)
    print('Non-Cancelled Characters: %s' % non_cancelled)

import collections

def leastInterval(tasks, n):
    counter = collections.Counter(tasks)
    print('counter', counter)
    result = 0


    while True:
        sub_count = 0
        # 개수 순 추출
        for task, _ in counter.most_common(n + 1):
            print("counter.most_common", counter.most_common(n + 1))
            print('task', task)
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하인 아이템을 목록에서 제거
            counter += collections.Counter()
            print(counter)
            print("----")
            print('sub_count', sub_count)
            print('result', result)

        if not counter:
            break

        result += n - sub_count + 1
        print('final_result', result)

    return result

if __name__ == '__main__':
    print(leastInterval(["A", "A", "A", "B", "C", "D"], 2))
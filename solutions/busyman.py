def interval_scheduling(start_list, end_list):
    result = list()

    index = list(range(len(start_list)))
    index.sort(key=lambda i: end_list[i])
    past_event_time = 0
    for i in index:
        if start_list[i] >= past_event_time:
            result.append(i)
            past_event_time = end_list[i]

    return result

if __name__ == "__main__":
    T = int(input())

    for index in range(T):
        N = int(input())

        start_list = list()
        end_list = list()

        if not N:
            break

        for index in range(N):
            start, end = map(int, input().split())
            start_list.append(start)
            end_list.append(end)

        result = interval_scheduling(start_list, end_list)
        print(len(result))
import doctest


def merge(intervals):
    """
    See https://leetcode.com/problems/merge-intervals/
    >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge([[1, 4], [4, 5]])
    [[1, 5]]
    """

    merged_intervals = [intervals[0]]

    for i in range(len(intervals)-1):
        first_interval_start, first_interval_end = merged_intervals[-1]
        second_interval_start, second_interval_end = intervals[i+1]
        if first_interval_end >= second_interval_start:
            interval_start = min(first_interval_start, second_interval_start)
            interval_end = max(first_interval_end, second_interval_end)
            merged_intervals[-1] = [interval_start, interval_end]
        else:
            merged_intervals.append([second_interval_start, second_interval_end])
    return merged_intervals


if __name__ == "__main__":
    doctest.testmod()

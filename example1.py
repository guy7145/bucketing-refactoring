# source:   lecture 6 (when not to use bucketing)
#
# 1. sum = 0
# 2. while (i < N) {
# 3.   sum += i;
# 4.   prod *= i;
# 5.   i++;
# 6. }

V = {1, 2, 3, 4, 5}
control_edges = {
    1: [],
    2: [3, 4, 5],
    3: [],
    4: [],
    5: []
}

data_edges = {
    1: [3],
    2: [3, 4, 5],
    3: [3, 5],
    4: [4, 5],
    5: [2, 4, 5]
}

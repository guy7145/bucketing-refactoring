# source:   https://github.com/jhy/jsoup/blob/master/src/main/java/org/jsoup/select/QueryParser.java
# file:     QueryParser.java
# method:   combinator(char combinator)
# lines: 85-100

V = {83, 85, 86, 87, 88, 90, 91, 92, 94, 95, 96, 100, 101}

control_edges = {
    83: [],
    85: [],
    86: [],
    87: [],
    88: [],
    90: [91, 92, 94, 100, 101],
    91: [],
    92: [],
    94: [95, 96],
    95: [],
    96: [],
    100: [],
    101: [],
}

data_edges = {
    83: [87],
    85: [91, 100],
    86: [92, 101],
    87: [],
    88: [96],
    90: [],
    91: [94],
    92: [95],
    94: [],
    95: [],
    96: [],
    100: [],
    101: [],
}

M = {96}

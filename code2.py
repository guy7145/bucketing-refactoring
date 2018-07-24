# source:   https://github.com/jhy/jsoup/blob/master/src/main/java/org/jsoup/parser/TokeniserState.java
# file:     TokeniserState.java
# method:   TokeniserState.RCDATAEndTagOpen.read
# lines: 201-211 (altough we can just use 203-206)

V = {202, 203, 204, 205, 206, 208, 209}


control_edges = {
    202: [203, 204, 205, 206, 208, 209],
    203: [],
    204: [],
    205: [],
    206: [],
    208: [],
    209: []
}

data_edges = {
    202: [],
    203: [],
    204: [],
    205: [],
    206: [],
    208: [],
    209: []
}

M = {204, 205}

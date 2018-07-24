# source: https://www.cs.bgu.ac.il/~icmr181/wiki.files/icmr172%20project%20by%20Pnina%20Nisisim%20and%20Guy%20Aviassaf%20and%20Noam%20Barkay.pdf
# pages 21-23
# We found a mistake the answer, run the code and you will find out...

V = {3, 4, 5, 6, 7, 8, 10, 13}

control_edges = {
    3: [4, 5, 13],
    5: [6, 7],
    7: [8, 10],
}

data_edges = {
    4: [5, 6, 7, 8]
}

M = {6, 8, 10, 13}

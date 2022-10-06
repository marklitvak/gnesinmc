d = {'Rb': '<a class="chessfig b">&#9820;</a>', 'Rw': '<a class="chessfig w">&#9820;</a>', 'Nw': '<a class="chessfig w">&#9822;</a>', 'Nb': '<a class="chessfig b">&#9822;</a>', 'Bb': '<a class="chessfig b">&#9821;</a>', 'Bw': '<a class="chessfig w">&#9821;</a>', 'Qb': '<a class="chessfig b">&#9819;</a>', 'Qw': '<a class="chessfig w">&#9819;</a>', 'Kb': '<a class="chessfig b">&#9818;</a>', 'Kw': '<a class="chessfig w">&#9818;</a>', 'Pb': '<a class="chessfig b">&#9823;</a>', 'Pw': '<a class="chessfig w">&#9823;</a>'}
f = open("out.txt", "w")
f.write('<div class="masonry__brick entry">\n')
f.write('\t<table class="chessboard">\n')
for i in range(8):
    line = list(input())
    f.write('\t\t<tr>\n\t\t\t')
    for e in line:
        if '1' <= e <= '8':
            f.write('<td></td> ' * int(e))
        else:
            f.write('<td>' + d[e] + '</td> ')
    f.write('\n\t\t</tr>\n')
f.close()
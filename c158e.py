# -*- coding: utf-8 -*-


    


for i in range(99):
    for j in range(99):
        if (i + j) ** 2 == i * 100 + j:
            if len(set(str(i).zfill(2) + str(j).zfill(2))) == 4:
                print "{0:2d}{1:02d}".format(i, j)
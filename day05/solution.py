import sys
import numpy as np


def convertLine(listInputPts, considerDiagonal) -> list:
    points = [[int(x) for x in pt.split(",")] for pt in listInputPts]
    diffVec = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
    if points[0][0] != points[1][0] and points[0][1] != points[1][1]:  # not x-y axis
        if not considerDiagonal:
            return None
        elif abs(diffVec[0]) != abs(diffVec[1]):  # not diagonal
            return None

    lenDiffVec = max(abs(diffVec[0]), abs(diffVec[1]))  # if one is 0 => non-zero value, if diag both equal
    absDiffVec = [int(diffVec[0]/lenDiffVec), int(diffVec[1]/lenDiffVec)]

    return [[points[0][0] + i*absDiffVec[0], points[0][1] + i*absDiffVec[1]] for i in range(0, lenDiffVec + 1)]


with open("input.in", "r") as f:
    coords = [line.split(" -> ") for line in f.read().splitlines()]
    dim = 10 if len(coords) == 10 else 1000
    mapThermalSimple = np.zeros((dim, dim))
    mapThermalComplex = np.zeros((dim, dim))
    for line in coords:
        outputPointsSimple = convertLine(line, False)
        outputPointsComplex = convertLine(line, True)
        if outputPointsSimple:
            for point in outputPointsSimple:
                mapThermalSimple[point[0]][point[1]] = np.nan if mapThermalSimple[point[0]][point[1]] == 0 else 1
        if outputPointsComplex:
            for point in outputPointsComplex:
                mapThermalComplex[point[0]][point[1]] = np.nan if mapThermalComplex[point[0]][point[1]] == 0 else 1

    print("Part 1: " + str(int(np.nansum(mapThermalSimple))))
    print("Part 2: " + str(int(np.nansum(mapThermalComplex))))
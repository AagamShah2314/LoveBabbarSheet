# 0.Rat In A Maze

from os import *
from sys import *
from collections import *
from math import *

def is_safe(i, j, arr, n):
    return (0<=i<n) and (0<=j<n) and arr[i][j]==1;

def find_paths(i, j, arr, n, path, paths):
    if i==n-1 and j==n-1:
        paths.append(path);
        return;
    arr[i][j] = -1;
    if is_safe(i+1, j, arr, n):
        find_paths(i+1, j, arr, n, path+'D', paths);
    if is_safe(i, j+1, arr, n):
        find_paths(i, j+1, arr, n, path+'R', paths);
    if is_safe(i-1, j, arr, n):
        find_paths(i-1, j, arr, n, path+'U', paths);
    if is_safe(i, j-1, arr, n):
        find_paths(i, j-1, arr, n, path+'L', paths);
    arr[i][j] = 1;

def searchMaze(arr, n):
    # Write your code here.
    paths = []
    if arr[0][0] == 1:
        find_paths(0, 0, arr, n, '', paths);
    return sorted(paths);
    pass

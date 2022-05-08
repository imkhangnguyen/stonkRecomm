from math import floor
import lib_import as lib
import collections
import random
import math

# companyList = ['Apple', 'Telsa', 'Nvidia','AMZN','GOOGL']
# companyscore =['10','-24','99','-17','55']
# companyScoreDict = dict(zip(companyList, companyscore))


def get_key(val, companyScoreDict):
    for key, value in companyScoreDict.items():
         if val == value:
             return key
 
    return "key doesn't exist"


def queue_up(companyList, companyScoreDict):

    
    myQueue =[]
    heap_size = [0]
    priorQueue = []
    returnQueue = []
    for item in companyList:
        #myQueue.append(companyScoreDict[item])
        insert(priorQueue, float(companyScoreDict[item]), heap_size[0], heap_size)

    #priorQueue = sorted(myQueue)

    for item in range(3):
        score = extract_max(priorQueue, heap_size[0], heap_size)
        name = get_key(score, companyScoreDict)
        returnQueue.append(name)
    
    return returnQueue


def maximum(arr):
    return arr[0]

def extract_max(arr, n, heap_size):
    if n > 0:
        heap_size[0] = n - 1
        max = arr[0]
        arr[0] = arr[n-1]
        max_heapify(arr, 1, n-1)
        return max

def increase_key(arr, i, k):
    if k < arr[i-1]:
        print('err, new key < current')
        return
    arr[i-1] = k
    par = math.floor(i/2)
    while i > 1 and arr[par-1] < arr[i-1]:
        arr[i-1], arr[par-1] =  arr[par-1], arr[i-1]
        i = par
        par = math.floor(i/2)

def insert(arr, k, n, heap_size):
    heap_size[0] = n + 1
    arr.append(float('-inf'))
    increase_key(arr, n+1, k)

def heap_sort(arr):
    build_max_heap(arr)
    for i in range(len(arr), 1, -1):
        arr[1-1], arr[i-1] = arr[i-1], arr[1-1]
        max_heapify(arr, 1, i-1)

def build_max_heap(arr):
    n = len(arr)
    for i in range(math.floor(n/2), 0, -1):
        max_heapify(arr, i, n)

def max_heapify(arr, i, n):
    l = 2*i
    r = 2*i + 1
    if l <= n and arr[l-1] > arr[i-1]:
        max = l
    else:
        max = i
    if r <= n and arr[r-1] > arr[max-1]:
        max = r
    if (max != i):
        arr[i-1], arr[max-1] = arr[max-1], arr[i-1]
        max_heapify(arr, max, n)
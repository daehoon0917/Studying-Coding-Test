# -*- coding: utf-8 -*-
"""Chapter 07 이진 탐색

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rdXP3_3IvDWGoxfUYYNUe85tKbrPXckk

7-1.py 순차 탐색 소스코드
"""

def sequential_search(n,target,array):
  for i in range(n):
    if array[i] == target:
      return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸 으로 합니다.")
array = input().split()

print(sequential_search(n,target,array))

"""7-2.py 재귀 함수로 구현한 이진 탐색 소스코드 """

def binary_search(array,target,start,end):
  if start > end:
    return None
  mid = (start + end) // 2
  if target > array[mid]:
    return binary_search(array,target,mid+1,end)
  elif target < array[mid]:
    return binary_search(array,target,start,mid-1)
  else:
    return mid

n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = int(binary_search(array,target,0,n-1))
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)

7-3.py 반복문으로 구현한 이진 탐색 소스코드

def binary_search(array,target,start,end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] > target:
      end = mid - 1
    elif array[mid] < target:
      start = mid + 1
    else:
      return mid

n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)

"""7-4.py 한 줄 입력받아 출력하는 소스코드"""

import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

"""실전 문제 부품 찾기"""

N = int(input())
Store = list(map(int,input().split()))
M = int(input())
Client = list(map(int,input().split()))

def binary_search(array,target,start,end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] < target:
    return binary_search(array,target,mid+1,end)
  else:
    return binary_search(array,target,start,mid-1)


for i in range(0,M):
  result = binary_search(Store,Client[i],0,N-1)
  if result == None:
    print('no',end = ' ')
  else:
    print('yes',end = ' ')
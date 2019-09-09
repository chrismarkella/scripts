import random
import numpy as np

from collections import deque
from time        import perf_counter_ns
from typing      import Union, List, Deque, Tuple, Any
from datascience import *

def performance(data_structure: Union[List[str], Deque[str]], N: int) -> Tuple[int, int]:
  """
  Return the appending and popping time of N elements in nanoseconds.
  
  Parameters:
  -----------
  data_structure: List[str] or Deque[str]
  N: int

  Example:
  --------
  >>> lst = []
  >>> N = 10**6
  >>> performance(lst, N)
  (2447553119, 122637513)  
  It took 2447553119 nano seconds to append  1 Million elements and
  it took  122637513 nano seconds to pop all 1 Million elements.
  """
  
  # testing append times
  start_append = perf_counter_ns()

  for _ in range(N):
    character = chr(random.randint(0, 26) + ord('a'))
    data_structure.append(character)
  end_append = perf_counter_ns()

  # testing popping times
  start_pop = perf_counter_ns()

  while data_structure:
    data_structure.pop()

  end_pop = perf_counter_ns()

  append_time = end_append - start_append
  pop_time = end_pop - start_pop

  return (append_time, pop_time)

def output(append_time: int, pop_time: int, data_structure: Union[List[str], Deque[str]]) -> None:
  print('performance of %s' %(type(data_structure)))
  
  print('append time: %.2f seconds' %(append_time / 10**9))
  print('pop    time: %.2f seconds' %(pop_time / 10**9))

def type_name(variable: Any) -> str:
  """
  Return the type of the variable.
  
  Example:
  -------
  >>> lst = [1, 2, 3]
  >>> type(lst)
  <class 'list'>
  >>> type_name(lst)
  'list'
  >>> n = 5
  >>> type(n)
  <class 'int'>
  >>> type_name(n)
  'int'

  """
  return str(type(variable)).split("'")[1]

def test(data_structures: List[Union[List[str], Deque[str]]], sample_sizes: List[int]) -> Table:
  """
  Return the test results in a Table.
  """
  append_times, pop_times = [], []
  data_structure_labels = []
  elements = []

  for N in sample_sizes:
    print('%d elements' %(N))
    print('-' * 20)
    for ds in data_structures:
      append_time, pop_time = performance(ds, N)
      output(append_time, pop_time, ds)
      
      append_times.append(append_time)
      pop_times.append(pop_time)
      data_structure_labels.append(type_name(ds))
      elements.append(N)
      print()
    print()
    # print()

  table = Table().with_columns(
    'Data structure',    data_structure_labels,
    'Elements',          elements,
    'Append time(nano sec)', append_times,
    'Pop time(nano sec)',    pop_times
  )
  return table

def main():
  sample_sizes = [10**5, 2*10**5]
  lst: List[str] = []
  my_stack: Deque[str] = deque()

  table = test([lst, my_stack], sample_sizes)
  table.set_format([1, 2, 3], NumberFormatter)
  print(table)

if __name__ == '__main__':
  main()


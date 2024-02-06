from main import *
import math
def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36;
  assert simple_work_calc(20, 3, 2) == 230;
  assert simple_work_calc(30, 4, 2) == 650;
  assert simple_work_calc(10, 2, 5) == 14;
  assert simple_work_calc(20, 2, 5) == 28;
  assert simple_work_calc(30, 2, 5) == 46;

	

def test_work():
  assert work_calc(30, 2, 2, lambda n: n) == 128
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300 
  assert work_calc(30, 2, 2, lambda n: n) == 128
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(10, 2, 5, lambda n: 1) == 7
  assert work_calc(20, 2, 5, lambda n: n*n) == 436 
  assert work_calc(20, 2, 2, lambda n: 1) == 31  #Added code f(n) = 1
  assert work_calc(20, 2, 2, lambda n: n) == 92  #Added code f(n) = n
  assert int(work_calc(20, 2, 2, lambda n: math.log(n))) == 19 


def test_span():
  assert int(span_calc(30, 2, 2, lambda n: n)) == 56





  
def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work
  #create work_fn1(n)
  def work_fn1(n):
    a = 16
    b = 2
    c = 2
    f = lambda n:math.pow(n,c) # n^c
    return work_calc(n, a, b, f)
    
  # create work_fn2
  def work_fn2(n):
    a = 16
    b = 2
    c = 6
    f = lambda n:math.pow(n,c)
    return work_calc(n, a, b, f)
    
  res = compare_work(work_fn1, work_fn2)
  print("WORK COMPARE \n")
  return print_results(res)
  

	
def test_compare_span():
  def span_fn1(n):
    a = 16
    b = 2
    f = lambda n: 1
    return span_calc(n, a, b, f)

  def span_fn2(n):
    a = 16
    b = 2
    f = lambda n: math.log(n)
    return span_calc(n, a, b, f)

  def span_fn3(n):
    a = 16
    b = 2
    f = lambda n: n
    return span_calc(n, a, b, f)

  results = compare_span(span_fn1, span_fn2, span_fn3)
  print("SPAN COMPARE \n")
  return print_results(results)

test_compare_work()
test_work()
test_compare_span()

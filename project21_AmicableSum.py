from time import perf_counter
def sum_of_divisors(a):
    sum=0
    for j in range(1,a//2+1):
        if a%j==0:
            sum=sum+j
    return sum
t1=perf_counter()
sum_of_amicable=0
for i in range(2,10001):
   a=sum_of_divisors(i)
   b=sum_of_divisors(a)
   if i == b and i != a:
        sum_of_amicable +=i
print(sum_of_amicable)
t2=perf_counter()
print("elapsed_time",t2-t1)

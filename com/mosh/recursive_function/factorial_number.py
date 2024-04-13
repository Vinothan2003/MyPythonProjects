# recursive function -- > is function that will call itself function during the execution
#                    -- > it will break down the problem in to smaller,similar or sub problems
#                    -- > it will consist into two parts --> base case --> recursion case
#                    -- > Base case --> used to stop the recursion case without base case it will infinite
#                    -- > recursive case --> part of function that will call itself consist of modified agrument.
#                    recursive function at last lead to the base case to terminate the recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input(">"))
factorial_number = factorial(number)
print(factorial_number)

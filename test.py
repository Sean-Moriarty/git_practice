print("hello world")
# The only real point of this is to keep practicing Git in VSCode

# 5/21/20
my_string = "string variable"
my_int = 42
my_float = 3.14
my_bool = True

#bubble sort 6/1/20
# I'm not sure if this is the best way to do this in python
# but this is how I learned to do this in Java, JavaScript
# and I think this is how I did this in Ruby
def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

my_list = [5, 3, 22, 14, 1, 7]
sorted_list = bubble_sort(my_list)
print(sorted_list)

#function returning function
def make_function(num):
    def made_function(num):
        print("This function is brought to you by the number {num}".format(num=num))
    return made_function

new_function = make_function(42)
new_function(6)

# this is a better example of a function returning function
# also utilizes a homemade switch statement, since those don't
# exist in python (use dict and return dict.get(arg=key))
def get_math_function(operation):
    def add(num1, num2):
        return num1 + num2
    def sub(num1, num2):
        return num1 - num2
    def mul(num1, num2):
        return num1 * num2
    def div(num1, num2):
        return num1 / num2
    
    switch = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    
    return switch.get(operation, "Invalid Operation")

add_func = get_math_function("+")
print(add_func(3, 2))

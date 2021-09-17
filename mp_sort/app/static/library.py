from org.transcrypt.stubs.browser import *
import random

array = []

def bubble_sort(Array):
    n = len(Array)
    #pick the compared num
    for i in range(n-1):
        #pick the neighbor
        for j in range(n-1):
            if Array[j] > Array[j+1]:
                Array[j+1],Array[j] = Array[j],Array[j+1]
return Array

def gen_random_int(number, seed):
	random.seed(seed)
	array = []
	for i in range(number):
		a = random.randint(0,10)
		array.append(a)
	return array

def generate():
    global array
    number = 10
    seed = 200
    
    array = gen_random_int(number, seed) 
    
    array_str = ''
    for i in array:
        array_str = array_str + str(i) + ','
    array_str = array_str[:-1] + '.'
    	

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"
    document.getElementById("generate").innerHTML = array_str


def sortnumber1():

    global array
    new_array = array.copy()
    sorted_new_array = bubble_sort(new_array)
    array_str = ''
    for i in sorted_new_array:
        array_str = array_str + str(i) + ','
    array_str = array_str[:-1] + '.' 
    document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
    value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
    if value == "":
        window.alert("Your textbox is empty") 

	# Your code should start from here
	# store the final string to the variable array_str
    string_ls = value.split(',')
    num_ls = [] 
    for i in string_ls:
        i = i.strip()
        num = int(i)
        num_ls.append(num)
        
    array = bubble_sort(num_ls)
    
    array_str = ''
    for i in array:
        array_str = array_str + str(i) + ','
    array_str = array_str[:-1] + '.' 
    document.getElementById("sorted").innerHTML = array_str



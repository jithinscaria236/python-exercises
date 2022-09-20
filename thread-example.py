# Python program to illustrate the concept of threading importing the threading module
import threading


def print_cube(num):
	# function to print cube of given num
	print("Cube of {} : {}" .format(num,num * num * num))


def print_square(num):
	# function to print square of given num
	print("Square of {} : {}" .format(num,num * num))


if __name__ =="__main__":
    try:
        # creating thread
        number = int(input("Enter an integer number: "))
        t1 = threading.Thread(target=print_square, args=(number,))
        t2 = threading.Thread(target=print_cube, args=(number,))

        # starting thread 1
        t1.start()
        # starting thread 2
        t2.start()

        # wait until thread 1 is completely executed
        t1.join()
        # wait until thread 2 is completely executed
        t2.join()

        # both threads completely executed
        print("Threads execution completed!")
    except Exception as error:
        print(f"Error occured inside the program:{error}")
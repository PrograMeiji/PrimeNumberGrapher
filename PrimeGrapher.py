import math
from tkinter import *
import time


def main():  # main method
    input_take()


def input_take():  # function to determine spiral direction of the graph
    wind = setup_window()  # window function variable
    can = setup_canvas(wind)  # canvas function variable
    input_letter = input("Please enter spiral direction(L = left, R = right): ")
    if input_letter == "L":
        draw_left_dir(wind, can)
    elif input_letter == "l":
        draw_left_dir(wind, can)
    elif input_letter == "R":
        draw_right_dir(wind, can)
    elif input_letter == "r":
        draw_right_dir(wind, can)
    else:
        print("Invalid entry. Please try again.")
        input_take()


def setup_window():  # creates window for graphics
    window = Tk()
    window.geometry("1080x1080")
    return window


def setup_canvas(win):  # create canvas for animation
    canvas = Canvas(win)
    canvas.configure(bg="black")
    canvas.pack(fill="both", expand=True)
    return canvas


def prime(val):  # function is used to determine whether a number is prime or not and goes up to 10000
    if val == 1:
        return False
    if val == 2:  # 2 is prime
        return True
    if val % 2 == 0:  # if num is divisible by 2, it is not prime
        return False
    num = int(math.sqrt(val) + 1)  # we only need to check the numbers up to the sqrt of val to determine if it is prime
    # we have already checked 1 and 2, meaning 3 is our starting point for the iterative loop
    for i in range(3, num):  # num = sqrt + 1 so we check the sqrt of val
        if val % i == 0:
            return False
    return True  # var is prime


def draw_left_dir(w, c):
    # coordinates for graphing lines and circles, 540 is center of 1080x1080
    x1 = 540
    y1 = 540
    x2 = 540
    y2 = 540
    # variables for turning lines
    step = 1
    step_size = 10  # distance between steps, also line length
    step_num = 1  # number of steps in current direction
    turn_counter = 1  # number of times direction has changed
    state = 0  # states 0 through 3 represent each direction

    while step < 5000:
        if state == 0:  # x to the left
            x1 -= step_size
        elif state == 1:  # y upwards
            y1 -= step_size
        elif state == 2:  # x to the right
            x1 += step_size
        elif state == 3:  # y downwards
            y1 += step_size
        c.create_line(x1, y1, x2, y2, fill="white", width="1")
        if prime(step+1):  # the center of the graph is 1 so we need to start the check at 2
            c.create_oval(x1+5, y1+5, x1-5, y1-5, fill="white")
        w.update()
        time.sleep(0.001)  # slows animation down
        # save previous x and y
        x2 = x1
        y2 = y1
        if step % step_num == 0:  # explanation can be found in draw_right_dir() at bottom
            state = (state + 1) % 4
            turn_counter += 1
            if turn_counter % 2 == 0:
                step_num += 1
        step += 1

    c.mainloop()
    exit()


def draw_right_dir(w, c):
    # coordinates for graphing lines and circles
    x1 = 540
    y1 = 540
    x2 = 540
    y2 = 540
    # variables for turning lines
    step = 1
    step_size = 10
    step_num = 1
    turn_counter = 1
    state = 0  # states 0 through 3 represent each direction

    while step < 5000:
        if state == 0:  # x to the right
            x1 += step_size
        elif state == 1:  # y upwards
            y1 -= step_size
        elif state == 2:  # x to the left
            x1 -= step_size
        elif state == 3:  # y downwards
            y1 += step_size
        c.create_line(x1, y1, x2, y2, fill="white", width="1")  # create a line
        if prime(step + 1):
            c.create_oval(x1 + 5, y1 + 5, x1 - 5, y1 - 5, fill="white")  # create a circle at prime numbers
        w.update()
        time.sleep(0.001)  # slows animation down
        # save previous x and y
        x2 = x1
        y2 = y1
        if step % step_num == 0:  # turns the line when we have gone 1 more than previous 2 directions steps
            state = (state + 1) % 4  # changes states 0 - 3
            turn_counter += 1  # when we change direction, update turn counter
            if turn_counter % 2 == 0:  # when we turn twice, increase step size by 1
                step_num += 1
        step += 1  # increase step

    c.mainloop()
    exit()


if __name__ == "__main__":
    main()

from tkinter import font
import tkinter as tk
import random
import time

high_score = 0
score = 0
score_label = None
label_coll = []
new_high_score = False

def get_game_data():
    global high_score
    file_path = "GameData.txt"

    try:
        with open(file_path, "r") as file:
            high_score_line = file.readline().strip()
            high_score_line_list = high_score_line.split(':')
            high_score = int(high_score_line_list[1])

    except FileNotFoundError:
        print(f"file not fount: {file_path}")

    except Exception as e:
        print(f"an error occured: {e}")
              
def set_game_data():
    global high_score
    # high_score update at the end of the game in the GameData.txt file
    file_path = "GameData.txt"
    try:
        with open(file_path, "w") as file:
            file.write(f"high_score:{high_score}")

    except Exception as e:
        print(f"error in set_game_data(): {e}")

def create_grid(window, labels, score_label, field):
    global score
    labels.clear()
    score = 0

    print('create_empty_grid() is reached')
    custom_fontSize = font.Font(size=20)

    score_label.pack(side="top", anchor="center")

    frame = tk.Frame(window, padx=20, pady=50)
    frame.pack(side="bottom")


    # Create a 4x4 grid of labels
    for i in range(4):
        row_labels = []
        for j in range(4):
            label = tk.Label(frame, text="",font=custom_fontSize, height=5, width=7, borderwidth=1, relief="solid", padx=10, pady=5)
            label.grid(row=i, column=j)
            
            row_labels.append(label)
        labels.append(row_labels)

    # Center the grid by giving weight to rows and columns
    for i in range(4):
        frame.grid_rowconfigure(i, weight=1)

    for j in range(4):
        frame.grid_columnconfigure(j, weight=1)

    print_to_screen(field, label_coll)

def handle_game(window):
    global score, score_label, label_coll, new_high_score
    
    get_game_data()
    print('open_game_window() is reached')
    
    window.destroy()
    
    game_window = tk.Tk()
    game_window.title("2048")
    width = 600
    height = 600
    game_window.geometry(f"{width}x{height}")
    
    custom_title_fontSize = font.Font(size=20)
    game_window.focus_force()

    field = []
    for i in range(4):
        field.append([0] * 4)

    original_field = [row[:] for row in field]
    score_label = tk.Label(game_window, text=f"SCORE:{score}\tHIGH SCORE:{high_score}",font=custom_title_fontSize, padx=8, pady=5)
    
    add_new_number(field)
    add_new_number(field)
    create_grid(game_window, label_coll, score_label, field)

    

    def on_key_press(event):
        global high_score, score, score_label, new_high_score
        nonlocal field

        if event.keysym in ('a', 'Left'):
            field, flag = move_left(field)
        elif event.keysym in ('w', 'Up'):
            field, flag = move_up(field)
        elif event.keysym in ('d', 'Right'):
            field, flag = move_right(field)
        elif event.keysym in ('s', 'Down'):
            field, flag = move_down(field)    
        else:
            print("Invalid input.")
            return

        win = is_won(field)



        if win == True:
            if score > high_score:
                new_high_score = True
                high_score = score
            show_popup(game_window, "YOU WON!", field)
        elif check_lose(field):
            if score > high_score:
                new_high_score = True
                high_score = score
            show_popup(game_window, "YOU LOST!", field)
        
        if check_empty_cells(field):
            add_new_number(field)
        
        # Refresh the grid
        print_to_screen(field, label_coll)

    # Bind the key press event to the window
    game_window.bind('<Key>', on_key_press)

    # Start the Tkinter mainloop
    game_window.mainloop()

def check_empty_cells(field):
    for i in range(4):
        for j in range(4):
            if field[i][j] == 0:
                return True
    
    return False

def print_to_screen(field, labels):
    global score_label, score, high_score

    for i in range(4):
        for j in range(4):
            if field[i][j] == 0:
                labels[i][j].config(text=" ")
            else:
                labels[i][j].config(text=field[i][j])
            change_color(labels[i][j], field[i][j])
    
    score_label.config(text=f"SCORE:{score}\tHIGH SCORE:{high_score}")
    
def show_popup(window, line, field):
    global label_coll, high_score, new_high_score

    popup_window = tk.Toplevel(window)
    popup_window.title("2048")
    popup_window.focus_force()
    set_game_data()

    if new_high_score == True:
        message_label = tk.Label(popup_window, text=f"NEW HIGH SCORE: {high_score}")
        time.sleep(1)
        message_label.pack(padx=20, pady=10)
        new_high_score = False
    else:
        message_label = tk.Label(popup_window, text=line)
        message_label.pack(padx=20, pady=10)
    

    def close_btn_click():
        popup_window.destroy()
        window.destroy()

    def restart_btn_click():
        global score

        for i in range(4):
            for j in range(4):
                field[i][j] = 0
        
        score = 0
        add_new_number(field)
        add_new_number(field)
        print_to_screen(field, label_coll)
        popup_window.destroy()
        window.focus_force()


    
    close_button = tk.Button(popup_window, text="Close", command=close_btn_click)
    close_button.pack(pady=5)
    
    restart_button = tk.Button(popup_window, text="New Game", command=restart_btn_click)
    restart_button.pack(pady=5)

    popup_window.geometry("300x150")

    # Make the pop-up window modal to prevent interaction with the main window
    popup_window.grab_set()

    popup_window.mainloop()

def change_color(label, num):
    if num == 0:
        # brown - grayish
        label.config(bg="#A39171")
    elif num == 2:
        # rose
        label.config(bg="#EEC0C6")
    elif num == 4:
        # light blue
        label.config(bg="#00BBCC")
    elif num == 8:
        # pumpkin
        label.config(bg="#F17105")
    elif num == 16:
        # pink lavender
        label.config(bg="#D1B1C8")
    elif num == 32:
        # old rose
        label.config(bg="#AF7A6D")
    elif num == 64:
        # sea green
        label.config(bg="#488B49")
    elif num == 128:
        # bittersweet 
        label.config(bg="#F25757")
    elif num == 256:
        # violet
        label.config(bg="#B07BAC")
    elif num == 512:
        # green
        label.config(bg="#1C7C54")
    elif num == 1024:
        # red
        label.config(bg="#F42C04")
    elif num == 2048:
        # yellow - goldish
        label.config(bg="#EAEE00")

def add_new_number(field):
    row = random.randint(0, 3)
    column = random.randint(0, 3)

    while(field[row][column] != 0):
        row = random.randint(0, 3)
        column = random.randint(0, 3)
    
    field[row][column] = 2

def is_won(field):

    for i in range(4):
        for j in range(4):
            if(field[i][j] == 2048):
                return True
    
    return False
 
def check_lose(field):

    # looks for empty cells
    for i in range(4):
        for j in range(4):
            if(field[i][j]== 0):
                return False
    
    for i in range(3):
        for j in range(3):
            if(field[i][j]== field[i + 1][j] or field[i][j]== field[i][j + 1]):
                return False
    
    # maybe I do not need this two
    for j in range(3):
        if(field[3][j]== field[3][j + 1]):
            return False
 
    for i in range(3):
        if(field[i][3]== field[i + 1][3]):
            return False
        
    return True

def compress(field):
    changed = False

    new_field = []

    for i in range(4):
        new_field.append([0] * 4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if(field[i][j] != 0):
                 
                # if cell is non empty then
                # we will shift it's number to
                # previous empty cell in that row
                # denoted by pos variable
                new_field[i][pos] = field[i][j]
                 
                if(j != pos):
                    changed = True
                pos += 1

    return new_field, changed

def merge(field):
    global score, high_score, score_label
    changed = False
    merged_cells = set()

    for i in range(4):
        for j in range(3):
 
            # if current cell has same value as
            # next cell in the row and they
            # are non empty then
            if (field[i][j] == field[i][j + 1] and field[i][j] != 0) and (i, j) not in merged_cells:
                
                # add to score
                score = score + (field[i][j] * 2)

                # double current cell value and
                # empty the next cell
                field[i][j] = field[i][j] * 2
                field[i][j + 1] = 0
 
                # make bool variable True indicating
                # the new grid after merging is
                # different.

                merged_cells.add((i,j))
                merged_cells.add((i,j + 1))
                changed = True
 
    return field, changed

def reverse(field):
    new_field =[]
    for i in range(4):
        new_field.append([])
        for j in range(4):
            new_field[i].append(field[i][3 - j])
    return new_field

def transpose(field):
    new_field = []
    for i in range(4):
        new_field.append([])
        for j in range(4):
            new_field[i].append(field[j][i])
    return new_field

def move_left(grid):
 
    # first compress the grid
    new_grid, changed1 = compress(grid)
 
    # then merge the cells.
    new_grid, changed2 = merge(new_grid)
     
    changed = changed1 or changed2
 
    # again compress after merging.
    new_grid, temp = compress(new_grid)
 
    # return new matrix and bool changed
    # telling whether the grid is same
    # or different
    return new_grid, changed

def move_right(grid):
 
    # to move right we just reverse
    # the matrix
    new_grid = reverse(grid)
 
    # then move left
    new_grid, changed = move_left(new_grid)
 
    # then again reverse matrix will
    # give us desired result
    new_grid = reverse(new_grid)
    return new_grid, changed
 
def move_up(grid):
 
    # to move up we just take
    # transpose of matrix
    new_grid = transpose(grid)
 
    # then move left (calling all
    # included functions) then
    new_grid, changed = move_left(new_grid)
 
    # again take transpose will give
    # desired results
    new_grid = transpose(new_grid)
    return new_grid, changed
 
def move_down(grid):

 
    # to move down we take transpose 
    new_grid = transpose(grid)
 
    # move right and then again
    new_grid, changed = move_right(new_grid)
 
    # take transpose will give desired
    # results.
    new_grid = transpose(new_grid)
    return new_grid, changed

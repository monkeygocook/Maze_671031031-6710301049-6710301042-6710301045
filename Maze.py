import os
import time
import MazeMechHard as MMH
import MazeKhingEZ as MKE
import MazeKhingHard as MKH
import MazePunEZ as MPE
import MazePunHard as MPH


class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", "x", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(11, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "R"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        #keyboard.wait("")

    def printNext(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Next Level <<<<<")
        print("\n\n\n")

    def find_path(self):
        from Queue import Queue  

        queue = Queue()
        queue.enqueue((self.ply, []))  

        visited = set()  
        visited.add((self.ply.y, self.ply.x))

        while not queue.isEmpty():
            current_pos, path = queue.dequeue()

        
            if self.maze[current_pos.y][current_pos.x] == "E":
                return path

        
            directions = [("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1)]

            for direction, dy, dx in directions:
                next_y, next_x = current_pos.y + dy, current_pos.x + dx

                if self.isInBound(next_y, next_x) and (next_y, next_x) not in visited:
                    if self.maze[next_y][next_x] in [" ", "E"]:
                        queue.enqueue((pos(next_y, next_x), path + [direction]))
                        visited.add((next_y, next_x))

        return []  


    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "R"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "R"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "R"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "R"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:  # noqa: F811
        self.y = y
        self.x = x

if __name__ == '__main__':

    m = maze()
    m.print()

    path = m.find_path()

    # ให้ผู้เล่นเดินตามเส้นทาง
    for step in path:
        if step == "up":
            m.move_up()
        elif step == "down":
            m.move_down()
        elif step == "left":
            m.move_left()
        elif step == "right":
            m.move_right()
        m.print()  # แสดงผลเขาวงกต
        time.sleep(0.25)  # หน่วงเวลาเล็กน้อย
    m.printNext()
    time.sleep(2)
    
    m2 = MKE.maze()
    m2.print()
    path = m2.find_path()

    for step in path:
        if step == "up":
            m2.move_up()
        elif step == "down":
            m2.move_down()
        elif step == "left":
            m2.move_left()
        elif step == "right":
            m2.move_right()
        m2.print()  
        time.sleep(0.25)  
    m2.printNext()
    time.sleep(2)
    
    m3 = MPE.maze()
    m3.print()
    path = m3.find_path()

    for step in path:
        if step == "up":
            m3.move_up()
        elif step == "down":
            m3.move_down()
        elif step == "left":
            m3.move_left()
        elif step == "right":
            m3.move_right()
        m3.print()
        time.sleep(0.25)
    m3.printNext()
    time.sleep(2)

    #m4 = maze()
    #m4.print()
    #path = m4.find_path()

    #for step in path:
        #if step == "up":
            #m4.move_up()
        #elif step == "down":
            #m4.move_down()
        #elif step == "left":
            #m4.move_left()
        #elif step == "right":
            #m4.move_right()
        #m4.print()
        #time.sleep(0.25)
    #m4.printNext()
    #time.sleep(2)

    m5 = MKH.maze()
    m5.print()
    path = m5.find_path()

    for step in path:
        if step == "up":
            m5.move_up()
        elif step == "down":
            m5.move_down()
        elif step == "left":
            m5.move_left()
        elif step == "right":
            m5.move_right()
        m5.print()
        time.sleep(0.25)
    m5.printNext()
    time.sleep(2)    
    
    m6 = MPH.maze()
    m6.print()
    path = m6.find_path()

    for step in path:
        if step == "up":
            m6.move_up()
        elif step == "down":
            m6.move_down()
        elif step == "left":
            m6.move_left()
        elif step == "right":
            m6.move_right()
        m6.print()
        time.sleep(0.25)
    m6.printNext()
    time.sleep(2)  

    #m7 = maze()
    #m7.print()
    #path = m7.find_path()

    #for step in path:
        #if step == "up":
            #m7.move_up()
        #elif step == "down":
            #m7.move_down()
        #elif step == "left":
            #m7.move_left()
        #elif step == "right":
            #m7.move_right()
        #m7.print()
        #time.sleep(0.25)
    #m7.printNext()
    #time.sleep(2)
    
    m8 = MMH.maze()
    m8.print()
    path = m8.find_path()

    for step in path:
        if step == "up":
            m8.move_up()
        elif step == "down":
            m8.move_down()
        elif step == "left":
            m8.move_left()
        elif step == "right":
            m8.move_right()
        m8.print()
        time.sleep(0.25)
    m.printEND()
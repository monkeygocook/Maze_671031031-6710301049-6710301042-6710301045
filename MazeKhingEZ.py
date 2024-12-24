import os
import time

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", "X", "X"],
                    ["X", " ", "X", " ", " ", "X", "X"],
                    ["X", " ", "X", "X", " ", " ", " "],
                    ["X", " ", " ", "X", "X", "X", "X"],
                    ["X", "X", " ", "X", " ", " ", "X"],
                    ["X", " ", " ", "X", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", " ", " ", "X"],
                    ["X", "X", "X", "X", "X", "X", "X"],

            
                    ]
        self.ply = pos(9, 1)
        self.end = pos(3, 6)
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


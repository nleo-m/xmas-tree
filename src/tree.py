from time import sleep

class Tree:
    def __init__(self, tree_size = 4, offset = 32, space_count = 10):
        self.tree_size = tree_size
        self.offset = offset
        self.space_count = space_count

        self.draw_top()
        self.draw_base()
        self.draw_message()

    def draw_triangular_shape(self, step):
        tmp_space_count = self.space_count
        star_count = 1 + step * 2

        while tmp_space_count > 0:
            if tmp_space_count <= 2:
                star_count += 2
                tmp_space_count -= 2

            for o in range(self.offset - step):
                print(" ", end="")

            for s in range(int(tmp_space_count / 2)):
                print(" ", end="")

            for r in range(star_count):
                print("\33[32m", end="")
                print("*", end="")
                sleep(0.01)

            print("")

            tmp_space_count -= 2
            star_count += 2


    def draw_top(self):
        for i in range(self.tree_size):
            self.draw_triangular_shape(i)
            
    def draw_base(self):
        star_count = self.tree_size + 1

        for i in range(self.tree_size):
            for o in range(self.offset - int(self.tree_size / 2)):
                print(" ", end="")

            for s in range(int(self.space_count / 2)):
                print(" ", end="")

            for r in range(star_count):
                print("\33[33m", end="")
                print("*", end="")
                sleep(0.01)
            
            print("")

    def draw_message(self):
        print("\33[31m\n")
        print("░  ░░░░  ░        ░       ░░       ░░  ░░░░  ░░░░  ░░░░  ░  ░░░░  ░░      ░░░      ░░")
        sleep(0.15)
        print("▒   ▒▒   ▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒   ▒▒   ▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒")
        sleep(0.15)
        print("▓        ▓      ▓▓▓       ▓▓       ▓▓▓▓    ▓▓   ▓▓▓    ▓▓▓        ▓  ▓▓▓▓  ▓▓      ▓▓")
        sleep(0.15)
        print("█  █  █  █  ███████  ███  ██  ███  █████  ████████  ██  ██  █  █  █        ███████  █")
        sleep(0.15)
        print("█  ████  █        █  ████  █  ████  ████  ███████  ████  █  ████  █  ████  ██      ██")
        sleep(0.15)
        print("=====================================================================================")
        sleep(0.15)
        print("\33[39m", end="")
        print("                                                                               - L30 ")

tree = Tree()







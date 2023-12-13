tree_size = 6

for i in range(tree_size):
    space_count = 10
    star_count = 1 + i * 2
    offset = 32 - i
    while space_count > 0:
        if space_count <= 2:
            star_count += 2
            space_count -= 2

        for s in range(offset):
            print(" ", end="")

        for s in range(int(space_count / 2)):
            print(" ", end="")

        for s in range(star_count):
            print("*", end="")

        print("")

        space_count -= 2
        star_count += 2

space_count = 10
star_count = tree_size + 1
offset = 32 - int(tree_size / 2)
for i in range(tree_size):
    for s in range(offset):
        print(" ", end="")

    for s in range(int(space_count / 2)):
        print(" ", end="")

    for s in range(star_count):
        print("*", end="")
    
    print("")


print("\n")
print("░  ░░░░  ░        ░       ░░       ░░  ░░░░  ░  ░░░░  ░  ░░░░  ░░      ░░░      ░░")
print("▒   ▒▒   ▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒  ▒▒  ▒▒▒  ▒▒  ▒▒   ▒▒   ▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒")
print("▓        ▓      ▓▓▓       ▓▓       ▓▓▓▓    ▓▓▓▓▓    ▓▓▓        ▓  ▓▓▓▓  ▓▓      ▓▓")
print("█  █  █  █  ███████  ███  ██  ███  █████  █████  ██  ██  █  █  █        ███████  █")
print("█  ████  █        █  ████  █  ████  ████  ████  ████  █  ████  █  ████  ██      ██")
print("██████████████████████████████████████████████████████████████████████████████████")
print("██████████████████████████████████████████████████████████  █████       ██      ██")
print("██████████████████████████████████████████████████████████  █████▒▒▒▒▒  ██  ▒▒  ██")
print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓  ▓▓▓▓▓       ▓▓  ▒▒  ▓▓")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░░       ░░      ░░")









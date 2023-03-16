# Coin Flip Percentage
# The user runs the program. The program asks the user to enter "head" or "tail".
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail".
# The user does the same over and over again.
# In each cycle, the program should return the current percentage of heads in the program, similar
# to what you see in the screenshot above.
# Also, you should write each user entry (i.e., head or tail) in a text file using a with-context
# manager, one entry per line.

user_input = ""

while user_input != "exit":
    user_input = input("Flip a coin, heads or tails, or exit: ")

    if user_input != "exit":

        with open("files/coin_flips.txt", "r") as f:
            flips = f.readlines()

        flips.append(user_input)
        flip_count = len(flips)
        head_count = 0
        head_count = [head_count + 1 for flip in flips if flip.strip('\n') == "heads"]
        heads_perc = float(len(head_count))/float(flip_count) * 100
        print(f"Percentage of head flips = {heads_perc} %")

        with open("files/coin_flips.txt", "a") as f:
            f.write(user_input + '\n')

        #user_input = user_input.strip('\n')


flip = ""
flip_count = 0
heads = 0

while flip != "stop":
    flip = input("Flip a coin, heads or tails (type stop to end)? ")
    flip_count += 1
    if flip == "heads":
        heads += 1
    total = (heads/flip_count) * 100
    print("Heads: {}".format(total))


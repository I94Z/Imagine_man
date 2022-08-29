import random


def imagine_man(lenght):
    with open("words/adjs.txt", "r", encoding="UTF-8") as adjs_f:
        n_adjs = adjs_f.read().split(";\n")
    with open("words/verbs.txt", "r", encoding="UTF-8") as verbs_f:
        n_verbs = verbs_f.read().split("\n")
    with open("words/nouns_1.txt", "r", encoding="UTF-8") as nouns_1_f:
        n_nouns_1 = nouns_1_f.read().split("\n")
    with open("words/nouns_2.txt", "r", encoding="UTF-8") as nouns_2_f:
        n_nouns_2 = nouns_2_f.read().split("\n")
    first = random.choice(n_adjs)
    n_adjs.remove(first)
    if lenght == 1:
        return f"Представь {first} чела.\nКак к нему отнесёшься? {random.choice([':D', ':0', ';-;', ':)', ';)', ':>'])}"
    text = f"Представь {first} чела, "
    for i in range(lenght - 1):
        if random.choice([0, 0, 0, 1]):
            next = random.choice(n_adjs)
            n_adjs.remove(next)
            text += f" {next}"
        else:
            text += random.choice(["", "", "", "", " не"])
            next = random.choice(n_verbs)
            n_verbs.remove(next)
            text += f" {next}"
            if next[-1] == "с" or next[-2:] == "за" or next[-3:] == "над":
                next = random.choice(n_nouns_2)
                n_nouns_2.remove(next)
            else:
                next = random.choice(n_nouns_1)
                n_nouns_1.remove(next)
            text += f" {next}"
        if i == lenght - 2:
            text += f".\nКак к нему отнесёшься? {random.choice([':D', ':0', ';-;', ':)', ';)', ':>'])}"
        else:
            text += ","
    return text
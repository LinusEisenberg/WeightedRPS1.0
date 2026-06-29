import random
rock_win = int(input("What should be the rock payoff?\n"))
paper_win = int(input("What should be the paper payoff?\n"))
scissors_win = int(input("What should be the scissors payoff?\n"))
residue_factor = 0.99
a_rock_chance = random.random()
a_paper_chance = random.uniform(0.0, 1 - a_rock_chance)
a_scissors_chance = 1 - a_rock_chance - a_paper_chance
b_rock_chance = random.random()
b_paper_chance = random.uniform(0.0, 1 - b_rock_chance)
b_scissors_chance = 1 - b_rock_chance - b_paper_chance
a_rock_freq = [];
a_paper_freq = [];
a_scissors_freq = [];
b_rock_freq = [];
b_paper_freq = [];
b_scissors_freq = [];
rounds = 100000
for i in range (rounds):
    b_rock_chance *= residue_factor
    b_paper_chance *= residue_factor
    b_scissors_chance *= residue_factor
    paperEV = a_rock_chance * paper_win - a_scissors_chance * scissors_win
    rockEV = a_scissors_chance * rock_win - a_paper_chance * paper_win
    scissorsEV = a_paper_chance * scissors_win - a_rock_chance * rock_win
    if rockEV >= paperEV and rockEV >= scissorsEV:
        b_rock_chance += 1 - residue_factor
    elif paperEV >= scissorsEV:
        b_paper_chance += 1 - residue_factor
    else:
        b_scissors_chance += 1 - residue_factor
    a_rock_chance *= residue_factor
    a_paper_chance *= residue_factor
    a_scissors_chance *= residue_factor
    a_paperEV = b_rock_chance * paper_win - b_scissors_chance * scissors_win
    a_rockEV = b_scissors_chance * rock_win - b_paper_chance * paper_win
    a_scissorsEV = b_paper_chance * scissors_win - b_rock_chance * rock_win
    if a_rockEV >= a_paperEV and a_rockEV >= a_scissorsEV:
        a_rock_chance += 1 - residue_factor
    elif a_paperEV >= a_scissorsEV:
        a_paper_chance += 1 - residue_factor
    else:
        a_scissors_chance += 1 - residue_factor
    a_rock_freq.append(a_rock_chance)
    a_paper_freq.append(a_paper_chance)
    a_scissors_freq.append(a_scissors_chance)
    b_rock_freq.append(b_rock_chance)
    b_paper_freq.append(b_paper_chance)
    b_scissors_freq.append(b_scissors_chance)
a_rock_chance = round(sum(a_rock_freq)/rounds, 3)
a_paper_chance = round(sum(a_paper_freq)/rounds, 3)
a_scissors_chance = round(sum(a_scissors_freq)/rounds, 3)
b_rock_chance = round(sum(b_rock_freq)/rounds, 3)
b_paper_chance = round(sum(b_paper_freq)/rounds, 3)
b_scissors_chance = round(sum(b_scissors_freq)/rounds, 3)
print(a_rock_chance, a_paper_chance, a_scissors_chance)
print(b_rock_chance, b_paper_chance, b_scissors_chance)
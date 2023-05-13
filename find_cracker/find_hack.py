# Someone was hacking the score. Each student's record is given as an array
# The objects in the array are given again as an array of scores for each name and total score. ex>
#
# The scores for each grade is:
#
# A: 30 points
# B: 20 points
# C: 10 points
# D: 5 points
# Everything else: 0 points
# If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded.
# After all the calculations, the total score should be capped at 200 points.
#
# Returns the name of the hacked name as an array when scoring with this rule.

array = [
    ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
    ["name2", 120, ["B", "A", "A", "A"]],
    ["name3", 160, ["B", "A", "A", "A", "A"]],
    ["name4", 140, ["B", "A", "A", "C", "A"]]
]


def find_hack(array):
    hackers = []
    for num in range(0, len(array)):
        cur_arr = array[num]
        if cur_arr[1] > 200:
            hackers.append(cur_arr[0])
        else:
            cur_grades = cur_arr[2]
            cur_score = 0
            failing = False
            for grade in cur_grades:
                if grade == "A":
                    cur_score += 30
                elif grade == "B":
                    cur_score += 20
                elif grade == "C":
                    cur_score += 10
                    failing = True
                elif grade == "D":
                    cur_score += 5
                    failing = True
                else:
                    cur_score += 0
                    failing = True
            if failing is False and len(cur_grades)>4:
                cur_score += 20
            if cur_score != cur_arr[1]:
                hackers.append(cur_arr[0])
    return hackers



print(find_hack(array))
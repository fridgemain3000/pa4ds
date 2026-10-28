# Assignment
# Consider a list L of triplets (e, s, v) where *e* is a string with the name of a 
# university course, *s* is a student-id, and *v* is the grade of the student who passed the 
# exam of the course. Write a Python function summary(L) that returns a dictionary
# mapping:

# the pair (“avg”, e) to the average of grades for course e
# the pair (“top”, e) to the list of students that passed exam e with top score

######################################

# summary() function takes list as an input and returns a dictionary
def summary(L: list) -> dict:
    # Dictionaries to group grades by exam and store the final result.
    partitoned_L = {}
    aggregated_dict = {} 

    # Group students and grades (s, v) by creating a list for each course associated with key "e".
    for e, s, v in L:
        if e not in partitoned_L:
            partitoned_L[e] = []
        partitoned_L[e].append((s, v))

    # Iterate over each exam (each dictionary key) to calculate its average and find the top students.
    for e in partitoned_L:
        # Initialize accumulators for the sum of grades and the maximum score.
        total_sum = 0
        max_score = -1

        # Calculate the total sum of grades and identify the highest grade in the course.
        # "partitoned_L[e]" is the key associated with the list of (s, v) tuples for the course "e".
        for s, v in partitoned_L[e]:
            total_sum += v
            if v > max_score:
                max_score = v

        # Calculate the average and, if it has no decimal part, convert it to an integer with "int()".
        avg = total_sum / len(partitoned_L[e])
        if avg.is_integer():
            avg = int(avg)

        # Collect all students who achieved the top score into a list.
        top_students = []
        for s, v in partitoned_L[e]:
            if v == max_score:
                top_students.append(s)

        # Assign the tuple keys ("avg", e) and ("top", e) to the final dictionary.
        aggregated_dict[("avg", e)] = avg
        aggregated_dict[("top", e)] = top_students

    # Return the complete dictionary after processing all courses.
    return aggregated_dict    

# Expected output:
# summary([('pds', 1, 28), ('pds', 2, 25), ('pds', 3, 28), ('dm', 1, 22), ('dm', 3, 30)])
# {('avg', 'pds'): 27, ('avg', 'dm'): 26, ('top', 'pds'): [1, 3], ('top', 'dm'): [3]}
    




        


    
    
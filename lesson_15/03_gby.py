# Assignment
# Exercise 3. [grouping] Consider a list of dictionaries data. Each dictionary maps the
# course a student has passed to the grade obtained (>= 18). E.g.,
# [ 
# {‘pds’:20, ‘dm’: 30},
# {‘log’:28, ‘pds’:30}, 
# … 
# ]
# Develop a Python function:
# • gby(data) that returns a dictionary mapping every course to the average grade of 
# students who passed that course.

################################################

# Function that takes a list of dictionaries and returns a dictionary with each course and its average grade.
def gby(data: list) -> dict:    
    
    # Dictionaries to store the aggregated votes and the final result.
    aggregated_grade = {}

    # Final result dictionary 
    total_avg_dict = {}

    # Iterate through each student (dictionary) in the input list 'data'.
    for student in data:
        # It loops through each course and grade for that student.
        for course, grade in student.items():
            
            # If the course is not yet a key in the dictionary, it initializes it with an empty list.
            if course not in aggregated_grade:
                aggregated_grade[course] = []

            # It aggregates all grades for the same course into the 'aggregated_grade' dictionary.
            aggregated_grade[course].append(grade)

    # Iterate through each course in the 'aggregated_grade' dictionary.
    for course in aggregated_grade:

        list_of_grades = aggregated_grade[course] 

        # Calculates the average grade for the current course
        total_avg = sum(list_of_grades) / len(list_of_grades)

        total_avg_dict[course] = total_avg

    # for course, votes in aggregated_votes.items(): --> Shorter way to do the same thing
    #     total_avg_dict[course] = sum(votes) / len(votes)

    return total_avg_dict

# Expected output:
# gby([{'pds': 20, 'dm': 30}, {'log': 28, 'pds': 30}])
# {'pds': 25.0, 'dm': 30.0, 'log': 28.0}

        
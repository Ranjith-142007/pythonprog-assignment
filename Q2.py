marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

print("Marks List:", marks_list)
print("Type of list:", type(marks_list))
print("Marks Tuple:", marks_tuple)
print("Type of tuple:", type(marks_tuple))

print("Highest Marks:", max(marks_list))
print("Lowest Marks:", min(marks_list))

# Count marks that are at least 40 without using a loop.
count_at_least_40 = (marks_list[0] >= 40) + (marks_list[1] >= 40) + (marks_list[2] >= 40) + (marks_list[3] >= 40) + (marks_list[4] >= 40)
print("Students scoring at least 40:", count_at_least_40)

# Check each mark is between 0 and 100 without using a loop.
valid_marks = (0 <= marks_list[0] <= 100 and
               0 <= marks_list[1] <= 100 and
               0 <= marks_list[2] <= 100 and
               0 <= marks_list[3] <= 100 and
               0 <= marks_list[4] <= 100)
print("Are all marks valid?", valid_marks)

# Lists are mutable, so their elements can be changed.
marks_list[0] = 80
print("Modified List:", marks_list)

# Tuples are immutable, so their elements cannot be changed.
# Uncommenting the next line would raise a TypeError:
# marks_tuple[0] = 80
print("Original Tuple:", marks_tuple)

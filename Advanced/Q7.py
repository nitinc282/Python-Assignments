def dictionary_from_lists(students,subjects):
    Output={}
    for key in students:
        for value in subjects:
            Output[key]=value
    print(Output)

students=["Sam", "Alice", "Mona"] 
subjects=["Commerce", "Science", "Computer"]
dictionary_from_lists(students,subjects)


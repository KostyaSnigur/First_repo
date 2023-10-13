def split_list(grade):
        if not grade:
            return ([], [])
        
        average = sum(grade) / len(grade)
        lower = [test_score for test_score in grade if test_score <= average]
        upper = [test_score for test_score in grade if test_score > average]
        return (lower, upper)
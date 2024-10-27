class Students:
    def __init__(self, id, arr_grades_a, arr_grades_b):
        self.id = id
        self.arr_grades_a = arr_grades_a
        self.arr_grades_b = arr_grades_b

    def is_improved(self):
        improved = True
        has_subject = False

        for grade_a, grade_b in zip(self.arr_grades_a, self.arr_grades_b):
            if grade_a != -1 and grade_b != -1:
                has_subject = True
                if grade_b < grade_a:
                    improved = False

        return improved and has_subject
# שאלה 4
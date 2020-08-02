"""
@wangqinag
本类实现输入学生成绩，判断学生表现
"""
class Student(object):

    def __init__(self, name, score):

        self.name = name

        self.score = score

    def get_grade(self):

        if self.score >= 90:

            return 'A'

        elif self.score >= 70:

            return 'B'

        else:
            return 'C'
wang = Student('张三', 100)
print(wang.name,wang.get_grade())#打印学生姓名和成绩

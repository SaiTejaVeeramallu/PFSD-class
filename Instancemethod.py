class Student:
    college = "KL University"

    @classmethod
    def info(cls):
        return cls.college


print(Student.info())
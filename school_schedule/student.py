class Student:
    """ 
    attributes: 
       - name: str
       - grade: str
       - classes: list
    methods: 
       - add_class, param: STR
       - get_num_classes, no args
       - summary, no args
       - display_each_class()
    """
    
    def __init__(self, name, grade, classes=None):
        self.name = name 
        self.grade = grade
        self.classes = classes if classes else []

    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        self.display_each_class()
        return self.__str__()

    def display_each_class(self):
        for name in self.classes:
            print(name)

        #TO DO AUDREY: solution that adds to a string for classes
        # iter method 
        
    # def greeting(self):
    #     print("hi")
    #     self.compliment()
    
    def __str__(self):
        return f"Student {self.name}, {self.grade}, {self.classes}"

    # def compliment(self):
    #     print("Mikelle your nails look SO good")
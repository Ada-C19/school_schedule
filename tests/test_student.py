from school_schedule.student import Student
# from ..school_schedule.student import Student

# print(beyonce)

def test_class_added_to_class_list():
    #arrange
    beyonce = Student("beyonce", "senior", ["PHD in music"])
    class_name = "PHD in dance"

    #act
    result = beyonce.add_class(class_name)

    #assert
    assert result == ["PHD in music", "PHD in dance"]
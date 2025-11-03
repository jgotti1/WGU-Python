
    # Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    if name not in info:
        raise StudentInfoError("Student ID not found for " + name)
    return info[name]


def find_name(ID, info):
    for key, value in info.items():
        if value == ID:
            return key
    raise StudentInfoError("Student name not found for " + ID)


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }
    
    userChoice = input()    # 0 = find_ID(), 1 = find_name()

    try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)
        
    except StudentInfoError as excpt:
        print(excpt.message)

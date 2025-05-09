
# 1. Library Book Tracker
library = {}

def add_book(title, author, pages): 
    library[title] = {'Author' : author, 'Pages' : pages}

def find_book(tittle): 
    search = library.get(tittle, 'Book not found.')
    return search

def show_books():
    return list(library.keys())

# 2. Student Grade Manager
grades = {}
def add_student(name): 
    grades[name] = []

def add_grade(name, grade): 
    grades[name].append(grade)

def get_average(name):
    average = grades.get(name, [])
    return sum(average) / len (average)

# 3. Restaurant Menu Editor
def add_dish(): pass
def change_availability(): pass
def total_available_price(): pass

# 4. Warehouse Box Counter
def add_box(): pass
def update_quantity(): pass
def has_enough(): pass

# 5. Movie Rating System
def add_movie(): pass
def rate_movie(): pass
def average_rating(): pass

# 6. Online Course Tracker
def add_course(): pass
def update_enrollment(): pass
def filter_by_hours(): pass

# 7. To-Do List Organizer
def add_task(): pass
def complete_task(): pass
def filter_tasks(): pass

# 8. Digital Wallet
def add_expense(): pass
def total_spent(): pass
def expense_percentages(): pass

# 9. Pet Adoption Center
def add_pet(): pass
def find_by_species(): pass
def older_than(): pass

# 10. Gym Membership System
def register_member(): pass
def change_plan(): pass
def unpaid_members(): pass

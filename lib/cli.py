
#here is where you do cli commands
from models.model import *
import inquirer as inquirer
# from colorama import Fore, Back, Style
# questions = [
#   inquirer.List('size',
#                 message="What size do you need?",
#                 choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#             ),
# ]
# answers = inquirer.prompt(questions)
def displayCampaignMenu():
    questions = [
    inquirer.List('input4',
                    message="What would you like to do?",
                    choices=[('See total amount of donations for campaign by id',1), ('Return to main menu', 3)],
                ),
    ]
    answers = inquirer.prompt(questions)
    if answers["input4"] == 1:
        edit_questions = [
            inquirer.Text(name="id", message="Enter id of campaign")
        ]
        edit_answers = inquirer.prompt(edit_questions)
        campaign = Campaign.get_one(edit_answers["id"])
        total_donations = campaign.total_donations()
        print(f'total donations for this campaign: {total_donations}')

def displayDonationMenu():
    questions = [
    inquirer.List('input3',
                    message="What would you like to do?",
                    choices=[('See total amount of donations',1),('See count of donations',2),('Return to main menu', 3)],
                ),
    ]
    answers = inquirer.prompt(questions)
    if answers["input3"] == 1:
        total_donations = Donation.total_donations()
        print(f'total donations: {total_donations}')
       
    elif answers["input3"] == 2:
        count_donations = Donation.count_donations()
        print(f'count of donations: {count_donations}')


def displayDonorMenu():
    questions = [
    inquirer.List('input2',
                    message="What would you like to do?",
                    choices=[('Create Donor',1),('Edit Donor by id',2), ('Find Donor by id',3), ('Delete Donor by id', 4), ('Return to main menu', 5)],
                ),
    ]
    answers = inquirer.prompt(questions)
    if answers["input2"] == 1:
        createQuestions = [
            inquirer.Text(name="name", message="Enter name"),
            inquirer.Text( name="state", message="Enter state")
        ]
        createAnswers = inquirer.prompt(createQuestions)
        create_donor = Donor(createAnswers["name"], createAnswers["state"])
        create_donor.save_donor()
    elif answers["input2"] == 2:
        edit_questions = [
            inquirer.Text(name="id", message="Enter id of donor")
        ]
        edit_answers = inquirer.prompt(edit_questions)
        edit_donor = Donor.get_one(edit_answers["id"])
        print(edit_donor.name)
        # edit_donor.save_donor()
        edit_questions = [
            inquirer.Text(name="name", message="Enter new donor name")
        ]
        edit_answers = inquirer.prompt(edit_questions)
        edit_donor.patch_donor_name(edit_answers["name"])
    elif answers["input2"] == 3:
        edit_questions = [
            inquirer.Text(name="id", message="Enter id of donor")
        ]
        edit_answers = inquirer.prompt(edit_questions)
        edit_donor = Donor.get_one(edit_answers["id"])
        print(edit_donor.name)
    elif answers["input2"] == 4:
        delete_questions = [
            inquirer.Text(name="id", message="Enter id of donor")
        ]
        delete_answers = inquirer.prompt(delete_questions)
        delete_donor = Donor.get_one(delete_answers["id"])   
        delete_donor.delete_donor()
    # elif answers["input1"] == 5:


if __name__ == "__main__":
    print('''
    WELCOME TO YOUR PORTAL
    ''')
    while True:
        questions = [
        inquirer.List('input1',
                        message="What would you like to do?",
                        choices=[('See donors',1),('See donations',2), ('See campaigns',3), ('Exit', 4)],
                    ),
        ]
        answers = inquirer.prompt(questions)
        if answers["input1"] == 1:
            displayDonorMenu()
        elif answers["input1"] == 2:
            displayDonationMenu()
        elif answers["input1"] == 3:
            displayCampaignMenu()
        elif answers["input1"] == 4:
            break 



#         # if answers["input1"] == 1:
#         #     dev_input = input("Input your id? ")
#         # elif answers["input1"] == 2:
#         #     teach_input = input("Input your id? ")
#         #     user = Teacher.get_one(teach_input)
#         #     if user:
#         #         print(f"Hello {user.name}")
#         #         while True:
#         #             i2 = input('''
# 1) What would you like to do?
# # 1) See total donations for a donor by id
# # 2) See avg donation for a donor by id
# 1) Delete a donor - enter id of donor you want to delete
# 2) Edit a donor - enter id of donor you want to edit
# 3) See all donors -
# 4) Create a donor - insert xxx
# ''')
# 2) What would you like to do?

# 1) See total amount of donations
# 2) See count of donations
# 3) Exit
# ''')
# 3) What would you like to do?
# 1) See total amount of donations by campaign id
# 2) See graph of campaign by total donations
# 3) Exit
# ''')
#                     if i2 == "1":
#                         my_students = user.students()
#                         questions = [
#                         inquirer.List('student',
#                                         message="Which Student would you like to grade?",
#                                         choices=[(student.name,student) for student in my_students],
#                                     ),
#                         ]
#                         selected_student = inquirer.prompt(questions)
#                         print('\033[31m'+ f"DELETING {selected_student['student'].name}")
#                         print(Style.RESET_ALL)
#                         selected_student["student"].delete()
#                     elif i2 == "3":
#                         my_students = user.students()
#                         for student in my_students:
#                             print(student.name)
#                     elif i2 == "4":
#                         break
#             else:
#                 print("Not valid teacher id")
            
#         elif answers["input1"] == 3:
#             break
#         else:
#             print("Please have valid input")
#             break
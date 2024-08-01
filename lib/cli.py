
#here is where you do cli commands
from models.model import *
import inquirer as inquirer
import matplotlib.pyplot as plt

#here is my function for anything pertaining to selecting the campaign class

def displayCampaignMenu():
    questions = [
        inquirer.List('input4',
                      message="What would you like to do?",
                      choices=[('See total amount of donations and average for campaign by id', 1),
                               ('Show bar graph of total donations by campaign', 2),
                               ('Return to main menu', 3)],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers["input4"] == 1:
        edit_questions = [
            inquirer.Text(name="id", message="Enter id of campaign")
        ]
        edit_answers = inquirer.prompt(edit_questions)
        campaign = Campaign.get_one(edit_answers["id"])
        if campaign:
            total_donations = campaign.total_donations()
            print(f'Total donations for this campaign: {campaign._name} : $ {total_donations}')
        else:
            print("Campaign not found")
    elif answers["input4"] == 2:
        print (Campaign.plot_total_donations_by_campaign())

    elif answers["input4"] == 3:
        return
#here is my function for anything pertaining to the donation class

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

#here is the function for anything pertaining to the donor class and full crud of it
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



if __name__ == "__main__":
    print('''
    Welcome to...WE SAVE ANIMALS' CRM platform
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



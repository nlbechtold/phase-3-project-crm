## Project Description:

Welcome to WE SAVE ANIMALS! As a development manager, you will use this application to get quick snapshots of basic KPIs within our CRM database. The basic KPIs will include, total amount of donations, and how much each campaign has brought in, by inputting the campaign's unique id. This application will also allow you to edit a donor, delete a donor, update a donor, and search for a donor; all by their unique id. Data is the driving force in which to make informed decisions to further our mission and increase our total donations, so we can save every animal...
---

## Project Structure

Here is a breakdown/tree of all the files that will be used, but what do they do?

├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   └── model.py
        └── seed.py
        └── seeds.sql
    ├── cli.py
    ├── debug.py

As a development manager, the main files you should note are below, along with their description:

Model.py
-This file is mainly for our tech department, but if you are curious, it contains all the classes/objects(donor, donation, capmaign), along with  their respective attributes/properties/methods ( fields, validation rules, and technical processes of each class/object). If you have more of a tech background, here (along with the sql file below), is where you would create new fields for a donor/donation/campaign. Please consult the tech department before diving in.

Seed.py
-This file is also used mainly by our tech department. This file contains the "source of truth" for the data/instances (donor/donation/campaign records).

Seeds.sql
-Just as the two above, this is also mainly used by our tech department. If you are familiar or knowledgeable about SQL and python, here is where you would utilize sqlite3 and also input the data structures (listed in "model.py"), so this application can work.

Cli.py
-Here is your main menu where you will be able to generate total donations, donations by campaign id; as well as edit/read/update/delete a donor using their unique id. This will be explained more in the section below.

Debug.py
-Again, this is for the tech department, when you are testing your methods/properties (technical processes/validation rules). Please consult the tech department before use.

---

## How do I use the CLI to access KPIs/donor information?

Before you start, you must run the following commands in the terminal:

-pipenv install
-pipenv shell

-python lib/cli.py

---

You will then see the following set up in the terminal:

[?] What would you like to do?: 
 > See donors
   See donations
   See campaigns
   Exit
To access the different objects, simply use the arrow buttons and press enter to select which object you are trying to access:

See donors (here you will be able to select from the following, you just need to have the donor's uniqe id handy)
[?] What would you like to do?: 
 > Create Donor
   Edit Donor by id
   Find Donor by id
   Delete Donor by id
   Return to main menu

See donations (here you will be able to select from the follow)
[?] What would you like to do?: 
 > See total amount of donations
   See count of donations
   Return to main menu

See campaigns (here you will be able to select from the following, just have the uniqe id of the campaign)
[?] What would you like to do?: 
 > See total amount of donations and average for campaign by id
   Show bar graph of total donations by campaign
   Return to main menu


---



## Resources


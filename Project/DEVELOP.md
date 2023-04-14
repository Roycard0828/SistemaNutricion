# Development info.
This project is made with Django technologies, especially with Django and Django templates.
The reason for this is that this project doesn't required a big scalability, just will manage 
and automize the work of the client which is an individual person who doesn't need a complicated work.

## Technologias used.
- Django.
- Django templates.
- PostgreSQL database.

## Methodolgies used.
We use Extreme Programming to realize this project. We divided the whole project into four iterations.
Each iteration will realize a tangible part of the project.
- Iteration 1: Patients logic.
- Iteration 2: Medical history of the patients.
- Iteration 3: meals plan for the patients.
- Iteration 4: Appointments logic.

### Iteration 1.
In this iteration will be developed all the patients logic, including the following steps.
- Create the patients model.
- Create the patients' view with all the necesary methods (create, read, update, delete, readAll).
- Create the patients tempaltes and vinculate with the views.
- Make the necesary test. 
- Iteration 1 Finished 3/09/22

### Iteration 2.
In this iteration will be developed the Clinical History for the patients.
#### Requierements:
- a patient will has only one clinical history.
- The clinical history will follow the current format given by the client
- The clinical history will be downloaded in PDF format.
#### Steps:
- Create all the necesary models (the main model for the clinical history will be split into other models).
- Create the clinical history view with the necesary methods (create, read, delete, update).
- Create the clinical history templates following the format given by the client.
- Make the necesary tests.

### Iteration 3.
In this iteration will be developed the Appointments logic.
#### Requirements:
- The patient can has N appointments assigned that will be displayed in the patient profile.
- The appointments to be made will be displayed on a TodoList oder by date.
- The appintments may be finished, canceled or postponed.
- Each appointment will has a medical prescription assigned.
#### Steps:
- Create the appointment and prescription models.
- Create the appointment views with the necesary methods (create, update, delete, read) for appointment and prescription
- Create the necesary templates (TodoList view) and display in the patients profile.
- Make necesary tests.
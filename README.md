# Maintenance Management System

A professional Odoo custom addon designed to manage maintenance tickets, responsible users, maintenance models, and scheduled visit details.

## Project Overview
This project was developed as a business-oriented Odoo module to streamline internal maintenance operations. It helps organizations track tickets, assign responsibilities, monitor status updates, and record visit information related to each maintenance request.

The solution is structured to support a practical workflow for service teams and maintenance departments that need to handle incoming service requests efficiently and record operational history.

## Key Features
- Maintenance ticket creation and management
- Responsible user assignment
- Maintenance model tracking
- Ticket status workflow (New, In Progress, Done, Cancelled, Reopened)
- Visit details linked to each maintenance ticket
- Date tracking for service completion and visit records
- Odoo report generation for ticket documentation

## Main Models
- `maintenance.ticket` - Stores customer, model, responsible user, ticket status, and related visits
- `responsible.user` - Stores responsible personnel information
- `maintenance.model` - Stores the type or category of maintenance model
- `visit.details` - Stores visit-related information for a maintenance ticket

## Workflow
1. Create a maintenance ticket
2. Assign a customer and maintenance model
3. Assign a responsible user
4. Start and update the ticket status
5. Record visit details associated with that ticket
6. Mark the ticket as done or reopen if necessary

## Technology Stack
- Odoo
- Python
- XML Views
- CSV Access Rights
- QWeb Reporting

## Project Structure
- `models/` - Odoo model definitions
- `views/` - UI form and list views
- `security/` - Access control rules
- `reports/` - Report templates and report actions
- `__manifest__.py` - Module metadata and dependencies

## Installation
1. Place the `maintenance` folder inside your Odoo custom addons directory.
2. Update the addons path in your Odoo configuration.
3. Restart the Odoo server.
4. Go to Apps and install the `Maintenance` module.

## Example Use Case
A company receives service requests from customers. Each request is tracked as a maintenance ticket, assigned to a responsible team member, and linked to a maintenance model. Visits performed during the service process are recorded with a date and description, giving the business a complete operational record.

## Professional Summary for CV
`Developed a custom Odoo maintenance management module for tracking service tickets, assigning team responsibilities, monitoring progress, and recording visit details. The solution improved operational visibility and streamlined maintenance workflows through Odoo model design, form views, access rights, and report generation.`

## GitHub Publication Suggestion
This project is suitable for public GitHub presentation because it demonstrates:
- real-world business process automation
- custom Odoo development
- data model design
- UI and workflow implementation
- reporting features

To publish it professionally:
1. Create a public GitHub repository
2. Add this README file
3. Upload the `maintenance` module folder
4. Add a short project title and description
5. Include screenshots if available

## License
This project is provided for educational and portfolio purposes.

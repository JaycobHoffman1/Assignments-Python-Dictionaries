# Task 1: Customer Service Ticket Tracker (all inputs are case-insensitive)

service_tickets = {
    'Ticket001': {'Customer': 'Alice', 'Issue': 'Login problem', 'Status': 'open'},
    'Ticket002': {'Customer': 'Bob', 'Issue': 'Payment issue', 'Status': 'closed'}
}

def check_user_input(user_input):
    while True:
        try:
            input_to_check = input(user_input)

            if len(input_to_check) == 0:
                raise ValueError('Field cannot be blank.')
        except ValueError as v:
            print(v)
        else:
            return input_to_check
        
def open_new_service_ticket():
    print('\nOpen new service ticket:\n')

    if len(service_tickets) < 9:
        id_num = f'00{len(service_tickets) + 1}'
    elif len(service_tickets) > 8 and len(service_tickets) < 99:
        id_num = f'0{len(service_tickets) + 1}'
    else:
        id_num = len(service_tickets) + 1

    ticket_id = f'Ticket{id_num}'
    enter_name = 'Enter your name: '
    name = check_user_input(enter_name)
    describe_issue = 'Describe your issue: '
    issue = check_user_input(describe_issue)
    service_tickets[ticket_id] = {'Customer': name, 'Issue': issue, 'Status': 'open'}

    print('Ticket opened!')

def update_status():
    print('\nUpdate status of existing ticket:\n')

    while True:
        if len(service_tickets) == 0:
            print('No statuses to update. The system is empty.')
            break

        enter_ticket_id = 'Enter the ID of the ticket you wish to update \
(type "done" when you are finished updating tickets): '
        ticket_id = check_user_input(enter_ticket_id)

        if ticket_id.lower() == 'done':
            break

        if service_tickets.get(ticket_id.lower().capitalize(), False):
            ticket_id = ticket_id.lower().capitalize()
            service_tickets[ticket_id]['Status'] = 'closed' \
            if service_tickets[ticket_id]['Status'] == 'open' else 'open'

            print(f'{ticket_id}\'s status has been updated to "{service_tickets[ticket_id]['Status']}".')
        else:
            print(f'"{ticket_id}" was not found in the system.')

def display_tickets():
    print('\nDisplay tickets:\n')

    while True:
        if len(service_tickets) == 0:
            print('No tickets to display. The system is empty.')
            break

        try:
            filter_by = input('Enter the status you wish to filter by, \
or leave blank to display all tickets: ')
            filter_by = filter_by.lower()
            
            if filter_by != 'open' and filter_by != 'closed' and filter_by != '':
                raise ValueError('Please enter a valid input.')
        except ValueError as v:
            print(v)
        else:
            break

    for ticket_id, details in service_tickets.items():
        if filter_by in service_tickets[ticket_id]['Status']:
            print(f'\n{ticket_id}: ')

            for key, value in details.items():
                print(f'{key}: {value}')

print('Welcome to the Customer Service Ticket Tracker!')

while True:
    print('\nMenu:\n\
1. Open new service ticket\n\
2. Update status of existing ticket\n\
3. Display tickets\n\
4. Quit program\n')
    
    while True:
        try:
            menu_selection = int(input('Select a menu option by entering it\'s corresponding number: '))

            if menu_selection < 1 or menu_selection > 4:
                raise ValueError
        except ValueError:
            print('Please enter a valid numeric value and ensure the number has a corresponding menu option.')
        else:
            break

    if menu_selection == 1:
        open_new_service_ticket()
    elif menu_selection == 2:
        update_status()
    elif menu_selection == 3:
        display_tickets()
    elif menu_selection == 4:
        print('\nQuitting program. Thank you for using the Customer Service Ticket Tracker!')
        break
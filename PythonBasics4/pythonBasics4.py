# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE
    if len(emails) == 0:
        return contacts

    count = 0
    for x in emails:
        contacts[list(contacts.keys())[count]] = x
        count = count + 1

    return contacts

# # Part B.


def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE
    if len(contact_info) == 0:
        return contacts
    count = 0
    for x in contact_info:
        if len(x) == 0:
            return contacts
        contact = {
            "email": x[0],
            "phone": x[1]
        }
        contacts[list(contacts.keys())[count]] = contact
        count = count + 1

    return contacts

# # Part C.


def dict_2_array(contacts):
    # YOUR CODE HERE

    return

# todo: write function to compare if enter password and confirm password are the same
# todo: write method to check if username/email/phone number is already registered

import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from validate_email import validate_email
from password_strength import PasswordPolicy
import messageBox

e = 0

# function to check blanks
# todo: rewrite this function


def check_blank_field(check_field):

	if len(check_field) != 0:
		e = 1
		return messageBox.window(e)
	else:
		return True


# a function to validate passwords
def passwordValidator(input, confirm):

	policy = PasswordPolicy.from_names(
		length= 6,
		uppercase= 1,
		numbers= 1,
		special= 0,
		nonletters= 1,
	)

	if policy.test(input) == False:
		e = 3
	return messageBox.window(e)


# function validates emails
def email_validator(mail):

	# email_regex = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

	# if check_blank_fields(mail) == False:
		# if not re.match(mail):
			# return False

	if validate_email(mail):
		return True
	else:
		e = 2
		return messageBox.window(e)


# function validates phone number
def phone_number_validator(num):

	# phone_regex = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')

# if check_blank_fields(num) == False:
# if not re.match(num):
# return False

	if carrier._is_mobile(number_type(phonenumbers.parse(num))):
		return  True
	else:
		e = 4
		return messageBox.window(e)

def check_username(username):
	pass

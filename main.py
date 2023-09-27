#Print a greeting to the user 
print('Welcome to the Elite 101 Chatbot!\n')
#Get input from user about their name
name = str(input('What is your name? '))
print('Nice to meet you ' + name + '!\n')
#Get input from user about their age
age = int(input('How old are you? '))
#Print a variety of messages reacting to their age
if age <= 30:
  print('Oh...to be young again...')
elif age <= 60:
  print('You must have a ton of stories to tell!')
else:
  print('Wowzers')

#Ask user how the chatbot can help them
print('\nNow...what can I help you with?\n')

choice = 0
while choice != 4:
  print('\nChoose from the following options')
  print('1. Placeholder 1')
  print('2. Placeholder 2')
  print('3. Placeholder 3')
  print('4. Exit')

  choice = int(input('Enter a number from the options '))

  if choice == 1:
    print('Response corresponding to option 1')
  elif choice == 2:
    print('Response corresponding to option 2')
  elif choice == 3:
    print('Response corresponding to option 3')
  elif choice == 4:
    print('Ending Conversation...')
  else:
    print('Please enter a valid number')

print('Goodbye ' + name + '! I hope you enjoyed this experience!')
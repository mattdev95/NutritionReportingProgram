# set the global constants
EXIT_PROGRAM = 'x'
BACK = 'b'

# this is opening the text file
food_items = open("sample.txt", 'r')
# calling the empty list to be our 2d list
food_items_2d_list = []
for item_rows in food_items:
    # this will ignore comments in the list
    if not item_rows.startswith("#"):
        # the rstrip will remove whitespace characters, which is the item one line and replace which will create
        # a single list in the list for each item in the list.
        # the split, will make it is a list of strings
        item_rows = item_rows.rstrip('\n').split(', ')
        # this adds each list in the 2d list to the empty array
        food_items_2d_list.append(item_rows)
# this will then close the file
food_items.close()


# this is the welcome message
print('|-----Welcome to the nutrition reporting program.-----|')


# allow the user to pick from a main menu different options
def main():
    # this is to initialize the while loop
    op = ''
    print('')
    # this will make sure the user has entered the correct value
    while op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '6' and op != '7' and op != 'x':
        print('Select from the menu option to continue: \n' +
              '(1) Show number of meal records. \n' +
              '(2) Show list of food items. \n' +
              '(3) Show a report of the calorie content \n' +
              '(4) Show average serving weights \n' +
              '(5) Add new food item \n' +
              '(6) Print report of each meal type \n' +
              '(7) Query list to get saturated fat threshold. \n' +
              '(x) To exit the program')
        option = input('Please enter the option you require: ')
        # this allow the user to pick and run the different options
        if option == '1':
            items_num()
        elif option == '2':
            list_content()
        elif option == '3':
            calorie_count()
        elif option == '4':
            av_serve_weights()
        elif option == '5':
            add_item()
        elif option == '6':
            create_type_list()
        elif option == '7':
            sat_threshold()
        elif option.lower() == 'x':
            close_program()
        else:
            # having problems here, not allowing me to enter in the command prompt again.
            print('You have entered the wrong input')
            print('')


# end of function

# this function will count the number of items in the list and return the result to the user
def items_num():
    # this outputs the number of items in the 2d list, it will count each list in the multidimensional list
    print('The number of items in your list is', len(food_items_2d_list))
    # this will allow the user to go back
    while BACK == 'b':
        back = input('Please enter b to go back to main menu: ').lower()
        if back == 'b':
            main()
        else:
            print('You have entered the wrong input')
    # end if


# create a function that lists the contents of the file
def list_content():
    # this way allows the user to see new added items as well, the above way only prints what originally was in the
    # list.
    for list_con in range(len(food_items_2d_list)):
        # this gets each position of each list in the 2d list
        time_position = food_items_2d_list[list_con][0]
        type_position = food_items_2d_list[list_con][1]
        description_position = food_items_2d_list[list_con][2]
        serving_position = food_items_2d_list[list_con][3]
        calorie_position = food_items_2d_list[list_con][4]
        satfat_position = food_items_2d_list[list_con][5]
        # this prints out a list of items
        print(time_position, type_position, description_position, serving_position, calorie_position, satfat_position)

    # this will validate if they have entered the correct input.
    while BACK == 'b':
        back = input('Please enter b to go back to main menu: ').lower()
        if back == 'b':
            main()
        else:
            print('You have entered the wrong input')
    # end if


# this function will get the calorie count of the items in the list
def calorie_count():
    print('Report of total calorie content:')
    for cal in range(len(food_items_2d_list)):
        # this allows the amount of calories to be shown per found item
        print('The food name is:', food_items_2d_list[cal][2], 'The calorie content is:', food_items_2d_list[cal][4],
              sep='  ->  ')
    # this is the total calorie which is initialized
    total_cal = 0
    for total in range(len(food_items_2d_list)):
        # this equal to the calorie content location in the array and the total will increment each time.
        cal_count = food_items_2d_list[total][4]
        # this will increment the num of each array location in the 2d array every iteration of the loop.
        total_cal = total_cal + int(cal_count)
        # this will print the total sum of all the calories in the list, as it is out of the loop.

    print('The total calorie content is', total_cal)
    # this will validate if they have entered the correct input.
    # allow the user to go back to the main menu

    while BACK == 'b':
        back = input('Please enter b to go back to main menu: ').lower()
        if back == 'b':
            main()
        else:
            print('You have entered the wrong input')


# this will get the average serving weights and return to the user
def av_serve_weights():
    # output the average of the serving weight divided by the number of items in list.
    total_serving = 0
    for total in range(len(food_items_2d_list)):
        # this equal to the serving content location in the list and the total will increment each time.
        serving_weight = food_items_2d_list[total][3]
        # this will increment the num of each list location in the 2d list every iteration of the loop.
        total_serving = total_serving + int(serving_weight)
        # this will store the average of all the serving weights in the list.
    serving_average = total_serving / len(food_items_2d_list)
    print('The average serving weights are', serving_average, 'grams.')
    # this will validate if they have entered the correct input.
    while BACK == 'b':
        back = input('Please enter b to go back to main menu: ').lower()
        if back == 'b':
            main()
        else:
            print('You have entered the wrong input')


# this will allow you to add the item to the list
def add_item():
    # let the program let the user enter something herevv
    # setup the local variable to make sure the while loop is true, to stop it from going out of the loop
    time_value = 1
    type_value = 1
    desc_value = 1
    serving_value = 1
    kcal_value = 1
    sfat_value = 1

    # allow the user to input time
    add_time = input('Please enter the time: ')
    # while not equal to zero, it will keep going through the loop
    while time_value != 0:
        try:
            # this will check if the time format was entered correctly, by checking each index position of the string.
            if int(add_time[0]) >= 0 and int(add_time[1]) >= 0 and add_time[2] == ':' and int(add_time[3]) >= 0 \
                    and int(add_time[4]) >= 0:
                # if it is true, then break out of the loop
                time_value = 0
            else:
                print('You have entered the incorrect value, it must be in the form 00:00')
                add_time = input('Please enter the time: ')
        # if an error has occurred, them catch the error using except for index and value error.
        except IndexError:
            print('You have entered the wrong value, must be in form 00:00')
            add_time = input('Please enter the time: ')
        except ValueError:
            print('You have entered the incorrect value, it must be in the form 00:00')
            add_time = input('Please enter the time: ')

    # allow the user to input food type
    add_type = input('Please enter the meal type: ')
    # while not equal to zero, it will keep going through the loop
    while type_value != 0:
        # if the value entered is alphabetic, then it is true and will break out of the loop
        # this was to prevent a space being a non alpha character
        # this replaces the space(if there is one) and replace with no space
        # and to check if its alpha
        if add_type.replace(' ', '').isalpha():
            type_value = 0
        else:
            print('Please enter characters only!')
            add_type = input('Please enter the meal type: ')
    # allow the user to input description
    add_desc = str(input('Please enter the meal description: '))
    # while not equal to zero, it will keep going through the loop
    while desc_value != 0:

        # if the value entered is alphabetic, then it is true and will break out of the loop
        # this was to prevent a space being a non alpha character
        # this replaces the space(if there is one) and replace with no space
        # and to check if its alpha
        if add_desc.replace(' ', '').isalpha():
            desc_value = 0
        else:
            print('Please enter characters only!')
            add_desc = input('Please enter the meal description: ')
    # allow the user to input serving in grams
    add_serving = input('Please enter the meal serving in grams: ')
    # while not equal to zero, it will keep going through the loop
    while serving_value != 0:
        # if the value entered is digit, then it is true and will break out of the loop
        if add_serving.isdigit():
            serving_value = 0
        else:
            print('Please enter a number value only!')
            add_serving = input('Please enter the meal serving in grams: ')
    # allow the user to input calories
    add_kcal = input('Please enter the meal calories: ')
    # while not equal to zero, it will keep going through the loop
    while kcal_value != 0:
        # if the value entered is digit, then it is true and will break out of the loop
        if add_kcal.isdigit():
            kcal_value = 0
        else:
            print('Please enter a number value only!')
            add_kcal = input('Please enter the meal calories: ')
    # allow the user to input saturated fat
    add_sfat = input('Please enter the meal saturated fat content: ')
    # while not equal to zero, it will keep going through the loop
    while sfat_value != 0:
        # if the value entered is digit, then it is true and will break out of the loop
        if add_sfat.isdecimal():
            sfat_value = 0
        else:
            print('Please enter a decimal number only!')
            add_sfat = input('Please enter the meal saturated fat content: ')
    # this allows each entry to be inserted into a list
    empty_array = [add_time, add_type, add_desc, add_serving, add_kcal, add_sfat]
    # this list is then added to the 2d list
    food_items_2d_list.append(empty_array)
    # this will sort in ascending order based on time
    for time_form in range(len(food_items_2d_list[0])):
        food_items_2d_list.sort()
    # this will list out each position of the list for each list in the 2d list
    for position in range(len(food_items_2d_list)):
        # this points to the time location
        time_position = food_items_2d_list[position][0]
        type_position = food_items_2d_list[position][1]
        description_position = food_items_2d_list[position][2]
        serving_position = food_items_2d_list[position][3]
        calorie_position = food_items_2d_list[position][4]
        sfat_position = food_items_2d_list[position][5]
        # this will print out each line in the list without square brackets
        print(time_position, type_position, description_position, serving_position, calorie_position, sfat_position)

    # allow the user to go back to the main menu
    while BACK == 'b':
        back = input('Please enter b to go back to main menu: ').lower()
        if back == 'b':
            main()
        else:
            print('You have entered the wrong input')


# create a function that creates a list with all the types
def create_type_list():
    # this creates an empty list, so items can be added later
    food_type_list = []
    # for each list in the 2d list
    for types in range(len(food_items_2d_list)):
        # this gets the position of the food type in the list
        dif_types = food_items_2d_list[types][1]
        # this will append each food type to the list
        food_type_list.append(dif_types)
    # this will insert the list of types into the meal_type_num function
    meal_type_num(food_type_list)


# this will get the number of food items per list by matching with the food type with a dictionary
# f_l is the variable name which a list of types will be passed into it
def meal_type_num(f_l):
    # this creates an empty dictionary
    food_types = {}
    # for each food item in list, which will be passed into it
    for food in f_l:
        # this will check if the food type exists into the dictionary and count
        # the number of types which is found
        if food in food_types:
            # this will get the certain food type and count up all of
            # the number of times it appears in the dictionary
            # for each food type found
            food_types[food] = int(food_types[food]) + 1
        else:
            # if it does not exist, then set it to 1
            food_types[food] = 1
    print('')
    print('Report on the number of each food type')
    # for every key and value of the dictionary in the items in the dictionary
    for type_k, type_v in food_types.items():
        # this will print out each of the food types with there count number
        print('There are', type_v, type_k, 'types')

    # this will allow the user to go back
    while BACK == 'b':
        back = input('Please enter b to go back to main menu: ').lower()
        if back == 'b':
            main()
        else:
            print('You have entered the wrong input')


# this will allow the user to set a threshold and return the items within the limit you have set
def sat_threshold():
    # this will catch any wrong values which have been inputted
    # this will set a value for the while loop, to make sure no infinite loop
    end_loop = 1
    # if end_loop is not equal to zero
    while end_loop != 0:
        try:
            # allow the user to enter a fat threshold
            input_sat = float(input('Please enter the saturated fat threshold: '))
            # this will search through each row and find saturated fat which is higher then the value inputted
            for sat_item in range(len(food_items_2d_list)):
                if_inside = food_items_2d_list[sat_item][5]
                # if the saturated fat is greater than the values in the list, it will show only the values that
                # meet that condition
                if float(if_inside) > float(input_sat):
                    print(food_items_2d_list[sat_item][0], food_items_2d_list[sat_item][1],
                          food_items_2d_list[sat_item][2],
                          food_items_2d_list[sat_item][3], food_items_2d_list[sat_item][4], if_inside)
            # set y = 0, to break out of the validation
            end_loop = 0
        # if an error is found, force them to enter again
        except ValueError:
            print('You have entered the wrong value \n', 'It must be an decimal value', sep='')
            sat_threshold()
        # allow the user to go back to the main menu
    while BACK == 'b':
        back = input('Please enter b to go back to main menu: ').lower()
        if back == 'b':
            main()
        else:
            print('You have entered the wrong input')


# this will exit the program once the user prompts to
def close_program():
    while EXIT_PROGRAM == 'x' or EXIT_PROGRAM == 'X':
        print('The program has ended \n' +
              'Goodbye', end='')
        exit()


# this will run the main function
main()


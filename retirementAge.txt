##################################
# Full Retirement Age Program
# Cesar Carrillo
##################################

# Libraries
import math;

# Global Variables
RETIREMENT_AGES = [ (1937, (65, 0)),
                    (1938, (65, 2)),
                    (1939, (65, 4)),
                    (1940, (65, 6)),
                    (1941, (65, 8)),
                    (1942, (65, 10)),
                    (1943, (66, 0)),
                    (1954, (66, 0)),
                    (1955, (66, 2)),
                    (1956, (66, 4)),
                    (1957, (66, 6)),
                    (1958, (66, 8)),
                    (1959, (66, 10)),
                    (1960, (67, 0)) ];

MONTH_NAMES = [ "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December", ];

# Input for integers only
def inputInt(prompt):
    integer = input(prompt);

    # Verify string
    if(integer.isnumeric()):
       return int(integer); # if int then return it
    else:
        print("\nPlease enter an integer value\n");
        return inputInt(prompt); # if not call <this> again

# Returns the retirement age and month (YEAR, MONTH)
def findRetirementInfo(birthYear):
    # Go through the RETIREMENT_AGES list to
    # find and return the appropriate information
    for i in range(len(RETIREMENT_AGES)):
        year = RETIREMENT_AGES[i][0];
        age = RETIREMENT_AGES[i][1];

        if(birthYear == year):
            return age; # an exact match is found so return

        # because the list has a an ~11 year gap with no
        # months added this was the best way I thought to
        # check if the birthYear falls in that range
        # *for 1943 - 1954

        # make sure we are not at the end of the list
        # if so then return as there are no more years to check
        if(i >= len(RETIREMENT_AGES) - 1):
            return age;
        else:
            # check the current year (i) with the next year
            # if we are in between these years then we fall in
            # the range
            yearNext = RETIREMENT_AGES[i + 1][0];

            if(birthYear > year and birthYear < yearNext):
                return age;

# Get the birth info from user
def requestBirthInfo():
    year = inputInt("Birth Year: ");
    month = inputInt("Birth Month: ");

    # the return order goes YEAR (0) then MONTH (1)
    return (year, month);

# Calculate and return the retirementAge
def calculateRetirementDate(birthInfo, retirementInfo):
    # Calculate the retirement year and month by
    # adding the birthInfo and retirementInfo
    # in every function related to this program
    # the return order goes YEAR (0) then MONTH (1)
    retirementYear = retirementInfo[0] + birthInfo[0];
    retirementMonth = birthInfo[1] + retirementInfo[1];

    # If we are more than 12 months then adjust the year and months
    if(retirementMonth > 12):
        retirementYear += math.floor(retirementMonth / 12);
        retirementMonth -= 12;

    return (retirementYear, retirementMonth);

# Returns month name using given month number
def getMonthName(month):
    return MONTH_NAMES[month - 1];

# Prints the retirement information in a sentence
def printRetirementInfo(retirementInfo):
    retirementAge = retirementInfo[0];
    retirementMonth = retirementInfo[1];

    # Print Text
    retirementText = str(retirementAge);

    # Display months?
    if(retirementMonth > 0):
        retirementText += " and " + str(retirementMonth) + " months";

    print("Your full retirement age is", retirementText);

# Print the retirement date in a sentence
def printRetirementDate(retirementDate):
    print("this will be in", getMonthName(retirementDate[1]), "of", retirementDate[0]);


# Program Entry point
def main():

    running = True;

    print("Social Security Full Retirement Age Calculator");

    while(running):
        print("-----------------------------------");

        # Request info
        birthInfo = requestBirthInfo();

        # Calculate retirement age/month
        retirementInfo = findRetirementInfo(birthInfo[0]);

        # Print the info
        printRetirementInfo(retirementInfo);

        # Calculate the retirement date
        retirementDate = calculateRetirementDate(birthInfo, retirementInfo);

        # Print the retirement date
        printRetirementDate(retirementDate);

        # Ask if the program should keep running
        exitProgram = input("\nExit program? (Y/N) ").lower();

        if(exitProgram == 'y' or exitProgram == 'yes'):
            running = False;


main(); # Run
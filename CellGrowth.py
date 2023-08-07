# take the initial cell population as input
cells = int(input())
cells = cells * 2

# take the number of days as input
days = int(input())
days = days + 1
# initialize the day counter
counter = 1

#complete the while loop
while counter < days:

  # Daily message
  print("Day " + str(counter) + ": " +str(cells))
  counter = counter + 1
  cells = cells * 2
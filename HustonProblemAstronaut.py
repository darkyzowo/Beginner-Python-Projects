#Astronaut candidates to undergo tests
# To qualify they need:
#physical test > 90
# flight_test >=  85

physic_test = int(input())
flight_test = int(input())

final_result = (physic_test > 90) and (flight_test >= 85)
print(final_result)
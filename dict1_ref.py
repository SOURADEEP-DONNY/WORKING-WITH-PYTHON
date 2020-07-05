#SORTING WITH VALUES AND PRINTING KEYS

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
medal_count=sorted(medals , reverse=False, key = lambda k:medals[k])
print(medal_count)

print('\n\n')
#PROCESS REVERSED

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
medal_count=sorted(medals , reverse=True, key = lambda k:medals[k])
print(medal_count)

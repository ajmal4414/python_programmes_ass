#6. write a code to check if two strings match where one string contains wildcard characters
import fnmatch
list=['this', 'is','just','a','test']
filtered=fnmatch.filter(list,'th?s')
print(filtered)
print(list)
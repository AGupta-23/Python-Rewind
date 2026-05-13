# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects

s1=60
s2=57
s3=87

totalPercen=(s1+s2+s3)*100/300

if(totalPercen>=40 and (s1>33) and s2>33 and s3>33):
    print("PASSED")
else:
    print("FAILED")

# 6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

# Grade Calculator using match-case

marks = int(input("Enter your marks: "))

match marks // 10:   #gives floor division so 9/8/7 etc

    case 10 | 9:
        print("Grade: Ex")

    case 8:
        print("Grade: A")

    case 7:
        print("Grade: B")

    case 6:
        print("Grade: C")

    case 5:
        print("Grade: D")

    case _:
        print("Grade: F")
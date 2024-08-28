# if else if ladder

# >80 -> HD
# 70-80 -> D
# 60-70 -> C
# 50-60 -> P
# <50 -> F

marks = int(input("What are your marks?"))

if marks >= 80:
    print("HD")
elif marks >= 70:
    print("D")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("P")
else:
    print("F")
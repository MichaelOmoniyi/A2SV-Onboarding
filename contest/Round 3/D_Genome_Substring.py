# t = int(input())
# s = str(input())
# genome = "ACTG"
# prefix = ""
# operation = 0

# if len(s) > 4:
#     prefix = s[:len(s) - 4]
#     s = s[-4:]

# for i in range(4):
#     if s[i] != genome[i]:
#         charUnicode = ord(s[i])
#         while charUnicode != ord(genome[i]):
#             if charUnicode > ord(genome[i]):
#                 charUnicode -= 1
#             else:
#                 charUnicode += 1
#             operation += 1
# print(operation)

t = int(input())
s = str(input())
genome = "ACTG"
prefix = ""
operation = 0

if len(s) > 4:
    prefix = s[:len(s) - 4]
    s = s[-4:]

for i in range(4):
    if s[i] != genome[i]:
        charUnicode = ord(s[i])

        if charUnicode > ord(genome[i]):
            if (charUnicode - ord(genome[i])) > 13:
                while charUnicode != ord(genome[i]):
                    charUnicode -= 1
                    operation += 1
            elif (charUnicode - ord(genome[i])) < 13:
                while charUnicode != ord(genome[i]):
                    charUnicode += 1
                    operation += 1
        else:
            if (ord(genome[i]) - charUnicode) > 13:
                while charUnicode != ord(genome[i]):
                    charUnicode -= 1
                    operation += 1
            elif (ord(genome[i]) - charUnicode) < 13:
                while charUnicode != ord(genome[i]):
                    charUnicode += 1
                    operation += 1

print(operation)
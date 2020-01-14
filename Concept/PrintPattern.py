# # # #
# # # #
# # # #
# # # #

n = int(input("enter the value: "))
for i in range(n):
    for j in range(n):
        print("# ", end='')
    print('\n')

#
#   #
#   #   #
#   #   #   #
#   #   #   #   #

n = int(input("enter the value: "))
for i in range(n):
    for j in range(i+1):
        print("# ", end='')
    print('\n')

#   #   #   #   #
#   #   #   #
#   #   #
#   #
#

n = int(input("enter the value: "))
for i in range(n):
    for j in range(n-i):
        print("# ", end='')
    print('\n')
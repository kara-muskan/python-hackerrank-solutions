N = int(input())
my_list = []
for i in range(0, N):
	result = input().split()
  if result[0] == 'insert':
    my_list.insert(int(result[1]), int(result[2]))
  elif result[0] == 'print':
    print(my_list)
  elif result[0] == 'remove':
    my_list.remove(int(result[1]))
  elif result[0] == 'append':
    my_list.append(int(result[1]))
  elif result[0] == 'sort':
    my_list.sort()
  elif result[0] == 'pop':
    my_list.pop()
  else:
    my_list.reverse()

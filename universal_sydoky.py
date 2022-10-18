data = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],

  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],

  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

data2 = [
  [4,8,2,3,9,7,15,14,10,5,16,11,13,12,6,1],
  [1,5,11,9,6,10,12,16,7,13,8,3,15,14,2,4],
  [16,12,10,6,5,3,1,13,2,15,14,4,9,11,8,7],
  [13,15,7,14,2,8,4,11,9,12,1,6,16,10,5,3],

  [2,6,12,7,4,13,10,15,8,1,11,16,5,3,9,14],
  [8,3,15,10,14,11,7,2,13,9,6,5,12,4,1,16],
  [5,4,16,1,12,9,6,8,14,10,3,2,7,15,13,11],
  [11,14,9,13,3,16,5,1,15,4,12,7,2,6,10,8],

  [15,16,3,5,1,4,14,10,12,6,9,13,11,8,7,2],
  [7,9,14,2,16,15,3,5,1,11,4,8,6,13,12,10],
  [12,13,1,11,8,6,2,7,3,16,15,10,4,9,14,5],
  [6,10,4,8,13,12,11,9,5,7,2,14,3,1,16,15],

  [10,11,5,12,15,1,8,6,4,2,7,9,14,16,3,13],
  [9,2,13,4,11,14,16,3,6,8,5,1,10,7,15,12],
  [3,7,8,15,10,2,9,4,16,14,13,12,1,5,11,6],
  [14,1,6,16,7,5,13,12,11,3,10,15,8,2,4,9]
]

def UniversalChecker(data):
  sydoky_size = len(data[0])

  for line in range(sydoky_size):
    local_array_column = []
    for column in range(sydoky_size):
      try:
        local_array_column.append(data[column][line])
      except:
        print("// Не выполняется условие NxN")
        return False
  if sydoky_size != len(local_array_column):
    return False

  ideal_array = []
  for i in range(sydoky_size):
    ideal_array.append(i+1)

  Success = True

  blocks_sydoky = []
  blocks_size = int(sydoky_size ** 0.5)

  def check_block(shift_pos_line, shift_pos_column, data0):
    timeout_array = []
    for stroka in range(blocks_size): # возьмем первые n строки
      first_elements = 0
      for nomer in range(blocks_size):
        if first_elements < blocks_size:
          timeout_array.append(data0[stroka + shift_pos_column][nomer + shift_pos_line])
        else:
          break
        first_elements += 1
    blocks_sydoky.append(timeout_array)

  for column in range(0, blocks_size*blocks_size, blocks_size):
    for line in range(0, blocks_size*blocks_size, blocks_size):
      try:
        check_block(line, column, data)
      except:
        return False

  for column in range(sydoky_size):
    local_array_line = []
    for line in range(sydoky_size):
      local_array_line.append(data[column][line])
    local_array_line.sort()

    if local_array_line != ideal_array:
      print(local_array_line)
      return False

  for line in range(sydoky_size):
    local_array_column = []
    for column in range(sydoky_size):
      local_array_column.append(data[column][line])
    local_array_column.sort()

    if local_array_column != ideal_array:
      print(local_array_column)
      return False
  return Success

print(UniversalChecker(data2))
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

sydoky_size = len(data[0])

blocks_sydoky = []
blocks_size = int(sydoky_size ** 0.5)

for creator_blocks in range(sydoky_size): # создаем пустой двойной массив
  empty = [0] * sydoky_size
  blocks_sydoky.append(empty)

for block in range(blocks_size): # n блок
  for line in range(sydoky_size): # n линия
    counter = 0
    for number in range(sydoky_size): # n число
      if counter < blocks_size:
        blocks_sydoky[block][number] = data[line][number]
      counter += 1



print(blocks_sydoky)


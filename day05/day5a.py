raw_input = open("day05/input", "r").read()[:-1]
box_input, move_input = raw_input.split('\n\n')

# Parse the input for boxes
box_input = box_input.split('\n')[::-1]
box_len = int((len(box_input[0])+1)/4)
boxes = []
for i in range(box_len):
    boxes.append([])
    for j in range(len(box_input)-1):
        box = box_input[j + 1][(i * 4) + 1]
        if box != ' ':
            boxes[i].append(box)

# Parse the input for moves
move_input = move_input.split('\n')
moves = []
for move in move_input:
    msplit = move.split(' ')
    moves.append([int(msplit[1]), int(msplit[3]) - 1, int(msplit[5]) - 1])

# Execute the moves
for move in moves:
    for box_move in range(move[0]):
        moved = boxes[move[1]].pop()
        boxes[move[2]].append(moved)

# Get the answer
answer = ""
for box in boxes:
    answer += box[-1]

print(answer)
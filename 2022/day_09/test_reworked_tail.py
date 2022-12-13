from solution_1_reworked import move_tail

# head moves left, tail shouldn't move
head = [3,4]
tail = [4,3]
new_tail = move_tail(tail,head,True)
if new_tail != [4,3]:
    raise Exception("moved somewhere")
else:
    print("ok - didn't move properly")

# head moves diagonal, tail shouldn't move
head = [4,1]
tail = [3,0]
new_tail = move_tail(tail,head,True)
if new_tail != [3,0]:
    raise Exception("moved somewhere")
else:
    print("ok - didn't move diagonal")

# same row, move right
head = [2,0]
tail = [0,0]
new_tail = move_tail(tail,head,True)
if new_tail != [1,0]:
    raise Exception("moving right doesn't match")
else:
    print("ok - moved right")

# same row, move left
head = [0,0]
tail = [2,0]
new_tail = move_tail(tail,head,True)
if new_tail != [1,0]:
    raise Exception("moving left doesn't match")
else:
    print("ok - moved left")

# head moves up too far, tail should move up
head = [4,3]
tail = [4,1]
new_tail = move_tail(tail,head,True)
if new_tail != [4,2]:
    raise Exception("moving up didn't match")
else:
    print("ok - moved up")

# head moves down too far, tail should move down
head = [4,1]
tail = [4,3]
new_tail = move_tail(tail,head,True)
if new_tail != [4,2]:
    raise Exception("moving down didn't match")
else:
    print("ok - moved down")

# head moves right up, tail should move diagonally 1/1
head = [4,2]
tail = [3,0]
new_tail = move_tail(tail,head,True)
if new_tail != [4,1]:
    raise Exception("moving diagonally (pos,pos) didn't match")
else:
    print("ok - moved diagonally right up")

# head moves left up, tail should move diagonally -1,1
head = [2,4]
tail = [4,3]
new_tail = move_tail(tail,head,True)
if new_tail != [3,4]:
    raise Exception("moving diagonally (neg, pos) didn't match")
else:
    print("ok - moved diagonally left up")

# head moves right down, tail should move diagonally 1,-1
head = [4,2]
tail = [3,4]
new_tail = move_tail(tail,head,True)
if new_tail != [4,3]:
    raise Exception("moving diagonally (pos, neg) didn't match")
else:
    print("ok - moved diagonally right down")

# head moves left down, tail should move diagonally -1,-1
head = [2,2]
tail = [4,3]
new_tail = move_tail(tail,head,True)
if new_tail != [3,2]:
    raise Exception("moving diagonally (neg, neg) didn't match")
else:
    print("ok - moved diagonally left down")
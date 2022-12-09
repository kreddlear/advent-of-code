generally: numbers are always faster than strings, and all i cared about were the numbers - tracking coordinates using strings slowed my solution waaaay down at first.

# part 1

we don't really care about anything other than whether a tree is visible or not - aka whether it's the tallest tree from the edge. so we don't need to start per tree specifically, just start from each edge and work one way or another.

# part 2

if something is multiplied by zero it'll always be zero, so don't even bother running other functions if it's zero. also we only care about the biggest one.

i feel like there's an algorithmic way to handle this, but my solution worked and was fast so...i'll come back to that!
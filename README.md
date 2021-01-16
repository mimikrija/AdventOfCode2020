# :christmas_tree: :snake: :sparkles: Maja's Advent of Code 2020 :sparkles: :snake: :christmas_tree:

Ho, ho, ho, welcome to my 2020 Advent of Code repository!
This year, my goals are:

1. learn Python :snake:
1. improve my coding style / logic :ok_hand: (I use keyword `[TIL]` in my commit messages for new stuff I learned)
1. collect at least 23 :star: before Christmas Day 2020 :white_check_mark:

Feel free to comment my code if you think it will help me reach goals 1. and 2.!

This was the first Advent of Code challenge that I started (:star: and completed!! :star:) roughly in real time ([Day 20](https://adventofcode.com/2020/day/20) was the most difficult one and it took me a couple of days after Christmas to solve part 2). I also have repositories here for all previous events (most of which are still under construction): [2015](https://github.com/mimikrija/AdventOfCode2015) :star:, [2016](https://github.com/mimikrija/AdventOfCode2016) :hammer:, [2017](https://github.com/mimikrija/AdventOfCode2017) :hammer:, [2018](https://github.com/mimikrija/AdventOfCode2018) :hammer:, [2019](https://github.com/mimikrija/AdventOfCode2019) :hammer:, [2020](https://github.com/mimikrija/AdventOfCode2020) :star: :white_check_mark:.

## What I learned, what I still don't know

Legend:

:ambulance: - I don't fully understand either the logic or the implementation - HALP!

:hourglass_flowing_sand: - I think this could or should run faster, but I don't know how to optimize it!

:hammer: - Not completely satisfied with solution, but I know how (and plan to) fix it.

Puzzle | Solution(s) | Remarks |
---    |---    |----
[Day 1: Report Repair](https://adventofcode.com/2020/day/1) | [Python](python/01.py) | Some heavily nested dictionary comprehensions. The goal was to find two (or three) numbers from the input list which sum to 2020. Maybe I could have just created a function which returns a number instead of creating a dictionary of all sums?
[Day 2: Password Philosophy](https://adventofcode.com/2020/day/2) | [Python](python/02.py) | I learned about argument (un)packing via `*`.
[Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3) | [Python](python/03.py) | :hammer: I am not sure if my code clearly shows what it is doing. This might be worth a refactor.
[Day 4: Passport Processing](https://adventofcode.com/2020/day/4) | [Python](python/04.py) | Just a bunch of conditions a passport must satisfy in order do be valid. Straightforward!
[Day 5: Binary Boarding](https://adventofcode.com/2020/day/5) | [Python](python/05.py) | I learned about `translate` which translates strings in Python.
[Day 6: Custom Customs](https://adventofcode.com/2020/day/6) | [Python](python/06.py) | `Counter` from `collections` module was very useful in this puzzle.
[Day 7: Handy Haversacks](https://adventofcode.com/2020/day/7) | [Python](python/07.py) | :hammer: Maybe this was an unintentional DFS ?
[Day 8: Handheld Halting](https://adventofcode.com/2020/day/8) | [Python](python/08.py) | One of those classics with a list of instructions which need to be executed until we're sent out of the instruction range.
[Day 9: Encoding Error](https://adventofcode.com/2020/day/9) | [Python](python/09.py) |I think this one was also pretty straightforward.
[Day 10: Adapter Array](https://adventofcode.com/2020/day/10) | [Python](python/10.py) | Honestly I don't remember what I did there. I think I calculated the number of possible combinations between adapters and then multiplied everything to get the final result. Maybe I could have used `reduce` with `mul`?
[Day 11: Seating System](https://adventofcode.com/2020/day/11) | [Python](python/11.py) | :hammer: I think I failed to recognize that this is an airport-lounge variation of the Conway game of life. 160 lines of code seems too much, I must have overcomplicated something, so I would definitely like to redo this one.
[Day 12: Rain Risk](https://adventofcode.com/2020/day/12) | [Python](python/12.py) | An interesting variation of those 2D grid puzzles. Took me a while to figure out this whole 'waypoint' thing, but it actually reduces to a special case of the first part. Sort of. Used complex numbers to move in 2D (I love that).
[Day 13: Shuttle Search](https://adventofcode.com/2020/day/13) | [Python](python/13.py) | Part two has something to do with the [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem), but I didn't manage to figure out how exactly. My original attempts were closest to [this approach](https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/), but were futile because of a crucial ingredient in these types of puzzles (for example [2015 Day 20](http://adventofcode.com/2015/day/20)) - you need to step in increments of your desired divisor!
[Day 14: Docking Data](https://adventofcode.com/2020/day/14) | [Python](python/14.py) | If my memory serves me right, this one was pretty straightforward...
[Day 15: Rambunctious Recitation](https://adventofcode.com/2020/day/15) | [Python](python/15.py) | :hourglass_flowing_sand: This is the part where the "let's see what happens for a ridiculously high number of turns in part 2" thing began. I just used the same logic for part 2 and it worked, but I am sure there is some way to speed it up.
[Day 16: Ticket Translation](https://adventofcode.com/2020/day/16) | [Python](python/16.py) | Again, one of those "just read the description carefully and implement what it says". I'd say there's some rome for improvement here, but I am not bothered to do it now.
[Day 17: Conway Cubes](https://adventofcode.com/2020/day/17) | [Python](python/17.py) | Hyper Conway game of life (part 1 in 3 dimensions, part 2 in 4 dimensions). `itertools.zip_longest` was the key ingredient which enabled me to fully generalize the solution to work for both dimensions without duplicating any code. As with any Conway game of life puzzle - what really speeds things up and makes the code look nicer is to: use sets, keep only active cubes in the set, check only _relevant_ cubes (the neighbors of active cubes which could potentially become active).
[Day 18: Operation Order](https://adventofcode.com/2020/day/18) | [Python](python/18.py) | :hammer: I see that I used `deque` here, which I think is a good approach for the operation order puzzles. But, looking at the code I think I might have overcomplicated stuff. I don't even fully remember what I did. Might redo this one.
[Day 19: Monster Messages](https://adventofcode.com/2020/day/19) | [Python](python/19.py) | :hammer: Uggh, grammar stuff again. I just don't understand that stuff. I think the first part (some rules depend on others, you need to figure out all the rules) is similar to [2015 Day 7](http://adventofcode.com/2015/day/7) and I think I could do this in a neater way (DPF?). The second part I explained in the code comments, since it is recursive we need to figure out the logic and filter out the messages based on that logic. For example we can deduce what will be the length of the messages, etc.
[Day 20: Jurassic Jigsaw](https://adventofcode.com/2020/day/20) | [Python](python/20.py) | :hammer: :ambulance: :pray: :fire: :cry: :cold_sweat: Hardest puzzle ever! My solution was based on _a lot_ of assumptions. For example, if I found a side that matches, I would assume this is the only possible match. I converted sides into binary and then into decimal, generated all possible numbers based on wether the tile is flipped (rotation does not play a role because in part 1 we are just looking for the corner pieces). That was pretty useless for part 2. I still don't know why some parts of the code work. After all that effort, finding the sea monsters was the easiest part.
[Day 21: Allergen Assessment](https://adventofcode.com/2020/day/21) | [Python](python/21.py) | Dictionaries and sets. Part 2 was super fast because we only needed to print out found ingredients based on the sorted allergen keys.
[Day 22: Crab Combat](https://adventofcode.com/2020/day/22) | [Python](python/22.py) | :crab: :hourglass_flowing_sand: Ah, this is where we first met the awesome little fella, the most wholesome character ever, _small crab_. There are some simplifications that others found on does it make sense to even start a sub game but I did not delve into that. I think my implementation is ok, it helped me a lot to print everything as in the example to figure out what needs to happen in part 1, and, especially, part 2. I used `deque` for decks, makes sense, right? :crab:
[Day 23: Crab Cups](https://adventofcode.com/2020/day/23) | [Python](python/23.py) | :crab: :hourglass_flowing_sand: The biggest lesson learned here: for some puzzles, if you do not know which data structure to use, you are doomed. In this case, linked list was the choice needed. I implemented it using `dictionary`, where the key is the current cup and the value is the cup "linked" (ie. next to) the key cup. Curious about possible speed up of part 2. :crab:
[Day 24: Lobby Layout](https://adventofcode.com/2020/day/24) | [Python](python/24.py) | An art installation variation of the Conway game of life + we use a [hexagonal grid](https://www.redblobgames.com/grids/hexagons/) (hexagons are bestagons!!). I used the same approach as in [Day 17](https://adventofcode.com/2020/day/17) + cube coordinates for hexes. Very satisfying puzzle.
[Day 25: Combo Breaker](https://adventofcode.com/2020/day/25) | [Python](python/25.py) | :hourglass_flowing_sand: Just read the instructions and do what it says. Wondering about possible speed up.

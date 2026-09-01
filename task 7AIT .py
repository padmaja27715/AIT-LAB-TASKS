class MonkeyBananaProblem:
    def __init__(self, monkey_pos, box_pos, banana_pos):
        # Initial states
        self.monkey_pos = monkey_pos
        self.box_pos = box_pos
        self.banana_pos = banana_pos
        self.is_on_box = False
        self.has_banana = False
        self.actions = []

    def walk(self, target_pos):
        if self.monkey_pos != target_pos:
            self.actions.append(f"1. Walk from Location {self.monkey_pos} to Location {target_pos}.")
            self.monkey_pos = target_pos

    def push_box(self, target_pos):
        if self.box_pos != target_pos:
            if self.monkey_pos != self.box_pos:
                self.walk(self.box_pos)
            self.actions.append(f"2. Push the box from Location {self.box_pos} to Location {target_pos}.")
            self.box_pos = target_pos
            self.monkey_pos = target_pos

    def climb_box(self):
        if self.monkey_pos == self.box_pos and not self.is_on_box:
            self.actions.append(f"3. Climb onto the box at Location {self.box_pos}.")
            self.is_on_box = True

    def grasp_banana(self):
        if self.is_on_box and self.monkey_pos == self.banana_pos:
            self.actions.append(f"4. Grasp the banana hanging at Location {self.banana_pos}.")
            self.has_banana = True

    def solve(self):
        # Step 1: Move monkey to the box location
        self.walk(self.box_pos)
        
        # Step 2: Push the box to the banana location
        self.push_box(self.banana_pos)
        
        # Step 3: Climb the box
        self.climb_box()
        
        # Step 4: Grab the banana
        self.grasp_banana()
        
        return self.actions

# Execute Problem with Scenario Values
monkey_start = 0
box_start = 2
banana_start = 3

solver = MonkeyBananaProblem(monkey_start, box_start, banana_start)
plan = solver.solve()

# Output Results
print("--- SEQUENCE OF ACTIONS ---")
for action in plan:
    print(action)

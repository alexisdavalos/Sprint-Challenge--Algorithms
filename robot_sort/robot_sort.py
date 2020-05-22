class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        print(f'swapping item: {self._item} with: {self._list[self._position]}')
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item


    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """

        # boot up robot
        self.set_light_on()

        # check if robots given list has more than 1 value
        while self.can_move_right():
            print(f'robot marker: {self._list[self._position]}')
            print(f'robot item: {self._item}')
            print(f'robot list: {self._list}')
            # item = None
            # l = [15, 41, 58, 49, 26, 4, 28,] 

            # grabs an item to it's right
            # item starts at None and becomes first index in list
            # item = 15
            print('swap 1')
            self.swap_item()
            # item is 15 on first pass
            # update the robots position marker by +1
            # self._position = 1
            self.move_right()

            # check the current item to the one next to it
            # is 15 > 41 ?
            if self.compare_item() == -1:
                self.move_right()
            else:
                print('swap 3')
                self.move_left()
                self.swap_item()
                self.move_right()

            # # put whatever is now held back in the starting position, and then move right to repeat on the next set of neighbors
            # self.move_left()
            # self.swap_item()
            # self.move_right()

        # # reset to the leftmost position to start again
        while self.can_move_left():
            self.move_left()

       

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
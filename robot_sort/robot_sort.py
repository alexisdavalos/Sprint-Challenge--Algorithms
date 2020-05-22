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
        # print(f'swapping item: {self._item} with: {self._list[self._position]}')
        # print(f'swapping marker: {self._list[self._position]} with: {self._item}')
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
        #immediately cuts loop, essentially marks this as a robot action
        # self.set_light_on()

        # while self.light_is_on():
        #     #turns off light
        #     self.set_light_off()
        #     # traverses down the right side of the list starting from [0]
        #     while self.can_move_right():
        #         # print(f'STARTING robot list: {self._list}')
        #         # print(f'robot marker: {self._list[self._position]}')
        #         # print(f'robot item: {self._item}')
        #         # swap the first time since it's set to None by default
        #         self.swap_item()
        #         # print(f'updated robot list: {self._list}')
        #         self.move_right()
        #         # compare the item held by robot vs marker
        #         # if the item is greater than the robot's current marker
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             # print(f'updated robot list: {self._list}')
        #             self.move_left()
        #             # print(f'robot marker moved left: {self._list[self._position]}')
        #             self.swap_item()
        #             # print(f'updated robot list: {self._list}')
        #             self.move_right()
        #             # print(f'robot marker moved right: {self._list[self._position]}')
        #             self.set_light_on()
        #         # if the held item is less than the marker
        #         if self.compare_item() == -1:
        #             self.move_left()
        #             # print(f'robot marker moved left: {self._list[self._position]}')
        #             self.swap_item()
        #             # print(f'robot list: {self._list}')
        #             self.move_right()
        #             # print(f'robot marker moved right: {self._list[self._position]}')
        #     # check if light is on
        #     if self.light_is_on():
        #         # will break us out
        #         while self.can_move_left():
        #             self.move_left()
        # robot's light will turn on for every loop
        self.set_light_on()

        # light indicates that some change was made on the last pass, and it needs to be checked again for further changes
        # if no changes were made, then every entry is less than the neighbor to its immediate right. By definition, this means it is sorted.
        while self.light_is_on():
            #immediately cuts loop, essentially marks this as a robot action
            self.set_light_off()

             # traverses down the right side of the list starting from [0]
            while self.can_move_right():
                print(f'robot marker: {self._list[self._position]}')
                print(f'robot item: {self._item}')
                # on first iteration, swaps None with first item
                # moves the marker to the next index
                self.swap_item()
                self.move_right()
                print(f'UPDATED robot list: {self._list}')
                # if the item is greater than the robot's current marker
                if self.compare_item() == 1:
                    # swaps the items
                    self.swap_item()
                    print(f'GREATER THAN robot list: {self._list}')
                    # restarts action loop
                    self.set_light_on()
                
                # swap the None for new item
                self.move_left()
                self.swap_item()
                # move right for next loop
                self.move_right()
              

            # reset to the leftmost position to start again
            while self.can_move_left():
                self.move_left()



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [1,15,6,55,7]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
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
        self.swap_item()
        self.set_light_on()
        while self.light_is_on():
            self.set_light_off()
            while self.can_move_right():
                self.move_right()

                #check if item is greater than position's item
                if self.compare_item() == 1:
                    self.swap_item()
                    self.set_light_on()
                    self.move_left()
                    self.swap_item()
                elif self.compare_item() == None:
                    self.swap_item()
                # elif self.compare_item() == -1:
                #     self.move_left()
                #     self.swap_item()
                else:
                    self.move_left()
                    self.swap_item()

            while self.can_move_right() == False:
                if self.compare_item() == None:
                    self.swap_item()
                    while self.can_move_left():
                        self.move_left()
                    if self.light_is_on():
                        self.swap_item()
            
        return self._list
        






item = None

l = [4,2,3,1]

myRobot = SortingRobot(l)

print(myRobot.sort())


#original bubble sort:
# def bubble_sort(arr):
#     swap = True
#     while swap is True:
#         swap = False
#         for i in range(0, len(arr) - 1):
            
#             current_index = i 

#             #if current value is greater than next swap
#             if arr[current_index] > arr[current_index + 1]:
#                 current_val = arr[current_index]
#                 compare_val = arr[current_index + 1]

#                 arr[current_index] = compare_val
#                 arr[current_index + 1] = current_val

#                 swap = True

#     return arr

item = None

[4,3,2,1]

item = 4
[None, 3,2,1]

item = 3
       #R 
[None, 4, 2, 1]

item = None

[3,4,2,1]
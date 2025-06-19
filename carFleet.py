from typing import List 

position = [4,1,0,7]
speed = [2,2,1,1]
target = 10

# Solution - Optimal Approach 
# Time Complexity - O(n logn), as we are sorting the given position array
# Space Complexity - O(n), as we are storing the pair of position , speed for a car
def carFleet( target: int, position: List[int], speed: List[int]) -> int:
    pairs = [(position[i], speed[i]) for i in range(len(position))]
    # a car's position is always < than target at the start, so it's fine to start curtime at 0 
    # (no fleet will be at target at time 0)
    fleets = curtime = 0 
    for dist, speed in sorted(pairs, reverse=True):
        # Calculate how long each car would take to reach the target on its own
        destination_time = (target - dist)/speed
        if curtime < destination_time:
            fleets += 1
            curtime = destination_time
    return fleets

print(carFleet(position=position, speed=speed, target=target))
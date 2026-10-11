from collections import defaultdict, deque
from typing import List
from sortedcontainers import SortedList


class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packets = deque()
        self.packet_map = {}
        self.dest_packet = defaultdict(SortedList)

    def remove_first_packet(self):
        packet = self.packets.popleft()
        del self.packet_map[packet]
        self.dest_packet[packet[1]].discard(packet[2])
        return packet

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packet_map:
            return False
        if len(self.packets) == self.memoryLimit:
            self.remove_first_packet()
        self.packets.append((source, destination, timestamp))
        self.packet_map[(source, destination, timestamp)] = True
        self.dest_packet[destination].add(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.packets) == 0:
            return []
        packet = self.remove_first_packet()
        return [packet[0], packet[1], packet[2]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        r = self.dest_packet[destination].bisect_right(endTime)
        l = self.dest_packet[destination].bisect_left(startTime)
        return r - l
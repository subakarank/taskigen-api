from enum import Enum

class PriorityEnum(Enum):
    UNKNOWN = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    WISHLIST = 4

    @property
    def label(self):
        labels = {
            PriorityEnum.UNKNOWN: 'None',
            PriorityEnum.LOW: 'Low',
            PriorityEnum.MEDIUM: 'Medium',
            PriorityEnum.HIGH: 'High',
            PriorityEnum.WISHLIST: 'Wish'
        }
        return labels[self]

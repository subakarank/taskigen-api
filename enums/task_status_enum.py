from enum import Enum
class TaskStatusEnum(Enum):
    NO_PROGRESS = 'NO_PROGRESS'
    PLANNED = 'PLANNED'
    IN_PROGRESS = 'IN_PROGRESS'
    BLOCKED = 'BLOCKED'
    ICEBOX = 'ICEBOX'
    CLOSED = 'CLOSED'

    @property
    def label(self):
        labels = {
            TaskStatusEnum.NO_PROGRESS: 'None',
            TaskStatusEnum.PLANNED: 'Planned',
            TaskStatusEnum.IN_PROGRESS: 'In progress',
            TaskStatusEnum.BLOCKED: 'Blocked',
            TaskStatusEnum.ICEBOX: 'Icebox',
            TaskStatusEnum.CLOSED: 'Closed'
        }
        return labels[self]

    @property
    def is_open(self):
        open_statuses = [
            TaskStatusEnum.NO_PROGRESS,
            TaskStatusEnum.PLANNED,
            TaskStatusEnum.IN_PROGRESS,
            TaskStatusEnum.BLOCKED,
            TaskStatusEnum.ICEBOX,
        ]
        return self in open_statuses
    
    @property
    def is_closed(self):
        closed_statuses = [
            TaskStatusEnum.CLOSED,
        ]
        return self in closed_statuses
    
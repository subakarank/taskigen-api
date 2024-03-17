from enum import Enum

class UserStatus(str, Enum):
  REGISTERED = 'REGISTERED'
  ACTIVE = 'ACTIVE'
  DISABLED = 'DISABLED'
  INACTIVE = 'INACTIVE'

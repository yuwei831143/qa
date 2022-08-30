
"""常量的配置"""
from enum import Enum


class UserStatus(Enum):

    USER_ACTIVE = 1

    USER_IN_ACTIVE = 0


class UserRole(Enum):
    """用户的角色"""

    COMMON = 0

    ADMIN = 1

    SUPER_ADMIN = 2
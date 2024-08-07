import enum


class ERROR_MSG(enum.Enum):
    NO_MSG = (enum.auto(), "입력된 값 없어. 돌아가.")
    EXIST_TODO = (enum.auto(), "이미 존재하는 값이야. 돌아가.")

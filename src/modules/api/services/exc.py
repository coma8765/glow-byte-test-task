from uuid import UUID


class InvalidData(Exception):
    pass


class NotFound(Exception):
    object_uid: UUID

    def __init__(self, object_uid: UUID) -> None:
        self.object_uid = object_uid

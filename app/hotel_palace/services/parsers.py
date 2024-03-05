from uuid import UUID

class IDParser:
    @staticmethod
    def paser_ids_by_comma(ids: str) -> list[str]:
        return (
            [id.strip() for id in ids.split(',') if id] or [ids]
        )
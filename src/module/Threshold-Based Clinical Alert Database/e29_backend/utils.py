from datetime import datetime, timezone
<<<<<<< HEAD


def serialize_doc(doc: dict | None) -> dict | None:
=======
from typing import Any, overload


@overload
def serialize_doc(doc: None) -> None:
    ...


@overload
def serialize_doc(doc: dict[str, Any]) -> dict[str, Any]:
    ...


def serialize_doc(doc: dict[str, Any] | None) -> dict[str, Any] | None:
>>>>>>> b6d27b02ba80f89c4d912f982dc757e736d77ee5
    if not doc:
        return None
    payload = dict(doc)
    payload["_id"] = str(payload["_id"])
    return payload


<<<<<<< HEAD
def serialize_many(docs: list[dict]) -> list[dict]:
    return [serialize_doc(doc) for doc in docs if doc]
=======
def serialize_many(docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [serialize_doc(doc) for doc in docs]
>>>>>>> b6d27b02ba80f89c4d912f982dc757e736d77ee5


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def next_id(prefix: str, count: int) -> str:
    return f"{prefix}{count + 1:03d}"
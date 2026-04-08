from fastapi import APIRouter, HTTPException

from e29_backend.db import patient_groups_collection
from e29_backend.models import PatientGroupCreate
from e29_backend.utils import serialize_doc, serialize_many


router = APIRouter()


@router.get("/patient-groups")
def list_patient_groups() -> list[dict]:
    docs = list(patient_groups_collection().find({}).sort("group_id", 1))
    return serialize_many(docs)


@router.get("/patient-groups/{group_id}")
def get_patient_group(group_id: str) -> dict:
    doc = patient_groups_collection().find_one({"group_id": group_id})
    if not doc:
        raise HTTPException(status_code=404, detail="Patient-group not found")
    return serialize_doc(doc)


@router.post("/patient-groups")
def create_patient_group(payload: PatientGroupCreate) -> dict:
    if patient_groups_collection().find_one({"group_id": payload.group_id}):
        raise HTTPException(status_code=409, detail="group_id already exists")
    patient_groups_collection().insert_one(payload.model_dump())
<<<<<<< HEAD
    return serialize_doc(patient_groups_collection().find_one({"group_id": payload.group_id}))
=======
    created = patient_groups_collection().find_one({"group_id": payload.group_id})
    if not created:
        raise HTTPException(status_code=500, detail="Patient-group creation verification failed")
    return serialize_doc(created)
>>>>>>> b6d27b02ba80f89c4d912f982dc757e736d77ee5


@router.put("/patient-groups/{group_id}")
def update_patient_group(group_id: str, payload: PatientGroupCreate) -> dict:
    existing = patient_groups_collection().find_one({"group_id": group_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Patient-group not found")
    patient_groups_collection().update_one({"group_id": group_id}, {"$set": payload.model_dump()})
<<<<<<< HEAD
    return serialize_doc(patient_groups_collection().find_one({"group_id": payload.group_id}))
=======
    updated = patient_groups_collection().find_one({"group_id": payload.group_id})
    if not updated:
        raise HTTPException(status_code=500, detail="Patient-group update verification failed")
    return serialize_doc(updated)
>>>>>>> b6d27b02ba80f89c4d912f982dc757e736d77ee5


@router.delete("/patient-groups/{group_id}")
def delete_patient_group(group_id: str) -> dict:
    result = patient_groups_collection().delete_one({"group_id": group_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Patient-group not found")
    return {"deleted": group_id}
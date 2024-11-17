from models.compiled_quantitative_data import CompiledQuantitativeData
from sqlalchemy.orm import Session
from db import get_db
from models.schemas.compiled_quantitative_data import CompiledDataModel
from fastapi import APIRouter, Depends, Query
import json
from services.comp_quant_data_svc import CompiledQuantitativeDataService
from typing import List
from sqlalchemy import text

# from models.coil_base import CoilBase


class CompiledDataResource:
    def __init__(self):
        self.router = APIRouter(prefix="/compiled-data", tags=["CompiledDataResource"])

    def get_router(self):
        @self.router.get("/get-partner-univerisities")
        async def get_compiled_data(
            semesters: List[str] = Query(),
            db: Session = Depends(get_db),
            svc=CompiledQuantitativeDataService(),
        ):
            res = {}
            for i in range(len(semesters)):
                semester, year = semesters[i].split()
                res[f"{semesters[i]}"] = svc.get_unique_partners(db, semester, year)

            return res

        @self.router.get("/get-quantity-data")
        async def get_compiled_data(
            semesters: List[str] = Query(),
            db: Session = Depends(get_db),
            svc=CompiledQuantitativeDataService(),
        ):
            res = {}
            for i in range(len(semesters)):
                semester, year = semesters[i].split()
                res[f"{semesters[i]}"] = svc.full_query(db, semester, year)

            return res

        @self.router.put("/update-hard-coded")
        async def update_hard_coded(
            semester: str = Query(...),
            undergrad_fdoc: int = Query(None),
            grad_fdoc: int = Query(None),
            undergrad_ldoc: int = Query(None),
            grad_ldoc: int = Query(None),
            eligible_ee_credit: int = Query(None),
            received_ee_credit: int = Query(None),
            db: Session = Depends(get_db),
        ):
            update_fields = {}

            if undergrad_fdoc is not None:
                update_fields["undergrad_fdoc"] = undergrad_fdoc
            if grad_fdoc is not None:
                update_fields["grad_fdoc"] = grad_fdoc
            if undergrad_ldoc is not None:
                update_fields["undergrad_ldoc"] = undergrad_ldoc
            if grad_ldoc is not None:
                update_fields["grad_ldoc"] = grad_ldoc
            if eligible_ee_credit is not None:
                update_fields["eligible_ee_credit"] = eligible_ee_credit
            if received_ee_credit is not None:
                update_fields["received_ee_credit"] = received_ee_credit

            if not update_fields:
                return {"message": "No valid fields provided for update."}

            set_clause = ", ".join([f"{key} = :{key}" for key in update_fields.keys()])
            query = text(f"""
                UPDATE compiled_hard
                SET {set_clause}
                WHERE semester = :semester
            """)

            update_fields["semester"] = semester

            result = db.execute(query, update_fields)
            db.commit()

            if result.rowcount == 0:
                return {"message": f"Semester '{semester}' not found. No updates made."}

            return {"message": f"Semester '{semester}' updated successfully."}

                
        @self.router.post("/add-hard-coded")
        async def add_hard_coded(
            semester: str = Query(...),
            undergrad_fdoc: int = Query(None),
            grad_fdoc: int = Query(None),
            undergrad_ldoc: int = Query(None ),
            grad_ldoc: int = Query(None),
            eligible_ee_credit: int = Query(None),
            received_ee_credit: int = Query(None),
            db: Session = Depends(get_db),
        ):
            existing_entry = db.execute(
                text("SELECT 1 FROM compiled_hard WHERE semester = :semester"),
                {"semester": semester}
            ).fetchone()

            if existing_entry:
                return {"message": f"Semester '{semester}' already exists. No data added."}

            query = text(
                """
                INSERT INTO compiled_hard (
                    semester, 
                    undergrad_fdoc, 
                    grad_fdoc, 
                    undergrad_ldoc, 
                    grad_ldoc, 
                    eligible_ee_credit, 
                    received_ee_credit
                ) VALUES (
                    :semester, 
                    :undergrad_fdoc, 
                    :grad_fdoc, 
                    :undergrad_ldoc, 
                    :grad_ldoc, 
                    :eligible_ee_credit, 
                    :received_ee_credit
                )
            """
            )
            db.execute(
                query,
                {
                    "semester": semester,
                    "undergrad_fdoc": undergrad_fdoc,
                    "grad_fdoc": grad_fdoc,
                    "undergrad_ldoc": undergrad_ldoc,
                    "grad_ldoc": grad_ldoc,
                    "eligible_ee_credit": eligible_ee_credit,
                    "received_ee_credit": received_ee_credit,
                },
            )

            db.commit()

            return {"message": "Data added successfully"}
        
        @self.router.delete("/delete-by-semester")
        async def delete_by_semester(
            semester: str = Query(...),
            db: Session = Depends(get_db),
        ):
            query = text("""
                DELETE FROM compiled_hard
                WHERE semester = :semester
            """)
            result = db.execute(query, {"semester": semester})
            db.commit()

            if result.rowcount == 0:
                return {"message": f"No row found for semester '{semester}'. No deletion performed."}

            return {"message": f"Semester '{semester}' deleted successfully."}


        return self.router

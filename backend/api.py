from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from database.datatable import get_db, engine
from models.models import Province
from models.models import Admin
from pydantic import BaseModel
from Middleware.cors import setup_cors

app = FastAPI()
setup_cors(app)

class ProvinceOut(BaseModel):
    name: str
    code:int
 
class AdminOut(BaseModel):
    fullname:str
    email:str
    password:str




@app.get("/provinces/", response_model=List[ProvinceOut])
async def read_provinces(db: Session = Depends(get_db)):
    # Truy vấn dữ liệu từ cơ sở dữ liệu
    provinces = db.query(Province.name, Province.code).all()
    # Tạo danh sách các tỉnh với mỗi tỉnh biểu diễn bằng một dictionary
    # chứa cả trường "name" và "code"
    provinces_list = []
    for province in provinces:
        provinces_list.append({"name": province.name, "code": province.code})
    
    return provinces_list



@app.get("/admins/", response_model=List[AdminOut])
async def read_admins(db:Session = Depends(get_db)):
    admins = db.query(Admin.fullname, Admin.email, Admin.password).all()

    admins_list = []
    for admin_list in admins:
        admins_list.append({"fullname":admin_list.fullname,"email":admin_list.email,"password":admin_list.password})
    return admins_list
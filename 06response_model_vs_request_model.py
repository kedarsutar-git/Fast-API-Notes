from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from mockData import products



# Request Body
class ProductResponse(BaseModel):
    id: int
    name: str
    count: int = Field(ge=0,le=2000)
    Price : int  =Field(ge=100,le=1000000)


app = FastAPI()
@app.get("/user/{user_id}",response_model =ProductResponse)
def get_User(user_id:int):
    for oneproduct in products:
        if oneproduct["id"]==user_id:
            return oneproduct

    raise HTTPException(status_code=404,detail="prouct is not found")

    
# Response Body   
class productRequest(BaseModel):
    Status:str
    product : list["productRequest"]

@app.post("/productCreate",response_model=productRequest,status_code=202)

def productcreate(productData:productRequest):
    productData = productData.model_dump()
    products.append(productData)

    return {"Status":"Product is Created",
            "Product":products}

    



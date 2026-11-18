'''
Decorator	  HTTP Method	        Common Purpose
@app.get()	      GET	      Retrieve or read data from the server.
@app.post()	      POST	      Create new data or submit payloads.
@app.put()	      PUT	      Replace or completely update existing data.
@app.patch()	  PATCH	      Partially modify existing data.
@app.delete()	  DELETE	  Remove existing data from the server.
'''


# Get Method

from fastapi import FastAPI
from mockData import products
app = FastAPI()

@app.get("/Products/{product_id}")

def MetaProducts(product_id:int):
    for oneproduct in products:
        if oneproduct.get("id")==product_id:
            return oneproduct

    return {"Satatus":"Product is not found"}



# PostMethod
from dtos import productsDTO
app = FastAPI()

@app.post("/createProducts")
def createProducts(productData:productsDTO):
    productData = productData.model_dump()

    products.append(productData)
       
    return  {"Status":"Product is Done..!","Data":products}


# PutMethod 

@app.put("/update_product/{product_id}")

def update_product(productdata:productsDTO,product_id:int):
    for index, oneproduct in enumerate(products):
        if oneproduct.get("id")==product_id:
            products[index] = productdata.model_dump()


            return {"status":"product Updated Successfully..","product":productdata}

    return {
            "error":"product is not found for this id"
    }
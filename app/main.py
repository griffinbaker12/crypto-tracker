from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enums import Coin
from get_price import get_crytpo_price

app = FastAPI()

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin, adjust as needed
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Allow these HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def read_hello():
    return {"Hello": "World"}


@app.get("/coin/{coin}")
def read_coin(coin: Coin):
    price = get_crytpo_price(coin)
    print(coin, price)
    return {"coin": coin, "price": price}

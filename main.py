#!/usr/bin/env python3
import frontend
from fastapi import FastAPI

app = FastAPI()

frontend.init(app)

if __name__ == '__main__':
    print('Please start the app with the "uvicorn" command as shown in the start.sh script')
from fastapi import FastAPI, Request

app=FastAPI()

@app.middleware("http")
async def gaurdrails_middleware(request: Request, call_next):
    # This is a placeholder for the gaurdr rails middleware implementation.
    banned_words = ["hack", "malware", "exploit"]

    if any(word in await request.body().decode("utf-8").lower() for word in banned_words):
        return {"error": "Input contains banned words. Please revise your input."}

    response = await call_next(request)
    return response
    
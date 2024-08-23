import uvicorn 

from fastapi import FastAPI, BackgroundTasks 
from send_email import Email 


app = FastAPI(title='How to Send Email')

@app.get("/")
def index():
    return 'Hello World'


@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    email = Email()
    await email.send_email_async(
        subject='Hello World',
        email_to='moroabdul@outlook.com',
        body="Hello"
        )
    return 'Success'

@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    email = Email()
    email.send_email_background(background_tasks, 'Hello World',  'moroabdul@outlook.com.com', {'title': 'Hello World', 'name': 'John Doe'})
    return 'Success'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
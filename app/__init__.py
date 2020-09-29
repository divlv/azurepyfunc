import azure.functions as func
import logging

def main(req: func.HttpRequest) -> str:
    logging.info('Python HTTP trigger function processed a request.')
    user = req.params.get('user')
    return f'Hello, {user}!'
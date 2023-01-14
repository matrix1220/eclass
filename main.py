from fastapi import FastAPI
from eclass.service import EclassService
from eclass.fetcher.cookie_storage.adapters.file_cookie_storage import FileCookieStorage
from eclass.fetcher.core import Fetcher
from eclass.service.wrappers.fastapi import EclassServiceRouter
from dotenv import dotenv_values

config = dotenv_values(".env")
cookie_storage = FileCookieStorage()
fetcher = Fetcher(config['USERNAME'], config['PASSWORD'], cookie_storage)
eclass_service = EclassService(fetcher)
router = EclassServiceRouter(eclass_service)

app = FastAPI()
app.include_router(router)
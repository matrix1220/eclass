
from eclass.service import EclassService
from eclass.fetcher.adapter.shielded_fetcher import Fetcher
from eclass.service.wrappers.fastapi import EclassServiceRouter
from dotenv import dotenv_values

config = dotenv_values(".env")

fetcher = Fetcher(**config)
eclass_service = EclassService(fetcher)
router = EclassServiceRouter(eclass_service)
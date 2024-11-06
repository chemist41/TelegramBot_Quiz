import nest_asyncio
nest_asyncio.apply()


import asyncio
import logging
from teleg_bot import main

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    asyncio.run(main())
#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .
from decouple import config

try:
    ALWAYS_DEPLOY_LATEST = config("ALWAYS_DEPLOY_LATEST", default=False, cast=bool)
    ALLOW_ACTION = config("ALLOW_ACTION", default=True, cast=bool)
    APP_ID = config("APP_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = "5915590855:AAEsLgbtUrjlPGBZ17ArUJg7-RrBGUaBirg"
    CACHE_DL = config("CACHE_DL", default=False, cast=bool)
    CAP_DECO = config("CAP_DECO", default="◉")
    C_LINK = config("C_LINK", default="@Anime_Jinx")
    DATABASE_URL = config("DATABASE_URL", default="mongodb+srv://480p:encode@cluster0.7fgwrif.mongodb.net/?retryWrites=true&w=majority")
                    
    DBNAME = config("DBNAME", default=str(BOT_TOKEN.split(":", 1)[0]))
    DEV = 1322549723
    DL_STUFF = config("DL_STUFF", default="")
    DUMP_CHANNEL = config("DUMP_CHANNEL", default="-1001927832537")
    DUMP_LEECH = config("DUMP_LEECH", default=False, cast=bool)
    EABF = config("EABF", default=False, cast=bool)
    ENCODER = config("ENCODER", default="@Anime_Jinx")
    WORKERS = config("WORKERS", default=2, cast=int)
    FBANNER = config("FBANNER", default=True, cast=bool)
    FCHANNEL = config("FCHANNEL", default="-1001809935648")
    FCHANNEL_STAT = config("FCHANNEL_STAT", default="4")
    FCODEC = config("FCODEC", default="dual")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -c:v copy -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    FSTICKER = config("FSTICKER", default="")
    LOCK_ON_STARTUP = config("LOCK_ON_STARTUP", default=False, cast=bool)
    LOG_CHANNEL = config("LOG_CHANNEL", default="-1001927832537")
    OWNER = "5700625607"
    RELEASER = config("RELEASER", default="ANIMXT")
    TEMP_USERS = config("TEMP_USERS", default="1443454117")
    THUMB = config("THUMBNAIL", default="")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()

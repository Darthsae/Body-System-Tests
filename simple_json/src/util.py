def debugDict(aDict: dict) -> str:
    toReturn: str = "{\n"
    for key, value in aDict.items():
        toReturn += f" \"{key}\": {debugDict(value).replace("\n", "\n ") if value is dict else value},\n"
    return toReturn[:-2] + "\n}"
def extractExtension(f):
    result = ''
    ext = ''
    tempList = f.rsplit('.', 1)
    try:
        ext = tempList[1]
        result = ext.lower()
    except IndexError:
        result = "noExt"
    
    return result
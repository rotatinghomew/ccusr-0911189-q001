def versions(rows):
    result = {}
    for row in rows:
        if row['id'] in result or set(row['errors']) & set(row['clears']):
            raise ValueError('版本编号重复或同一错误同时被携带与澄清')
        result[row['id']] = row
    return result

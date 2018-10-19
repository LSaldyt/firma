def build_ast_dictionary(code, prefix=tuple(), d=None):
    if d is None:
        d = dict()

    if prefix == tuple():
        d['total'] = code
    else:
        d[prefix] = code
    tag, subcode = code
    if isinstance(subcode, list):
        for i, subitem in enumerate(subcode):
            build_ast_dictionary(subitem, prefix=prefix + (i,), d=d)

    return d

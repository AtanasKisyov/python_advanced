def age_assignment(*args, **kwargs):
    res = {}
    for name in args:
        for initial, age in kwargs.items():
            if name.startswith(initial):
                res[name] = age
    return res

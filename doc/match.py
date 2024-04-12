def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not Allowed"
        case 404:
            return "Not found"
        case 418:
            return "Im a teapot"
        case _:
            return "Something's wrong with the internet"

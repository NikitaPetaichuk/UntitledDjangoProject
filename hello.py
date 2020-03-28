def wsgi_application(environ, start_response):
    response_data = bytes("\r\n".join(environ["QUERY_STRING"].split("&")), encoding="uft8")
    start_response("200 OK", [("Content-Type", "text/plain")])
    return iter([response_data])

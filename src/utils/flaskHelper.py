from flask import jsonify, make_response


def set_resp_data(respData):
    headers = {"Access-Control-Allow-Origin": "*"}
    respDataJson = jsonify(respData)
    resp = make_response(respDataJson, 200, headers)
    return resp


def set_correct_result(data):
    return {'status': 1, 'data': data}


def set_error_result(data):
    return {'status': 0, 'data': data}
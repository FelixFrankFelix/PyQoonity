from utility.exceptions import ResponseConstant


def create_user_service(body):
    if not body:
        return {
        "responseCode": ResponseConstant.DUPLICATE_RECORD.responseCode,
        "responseMessage": "email already exist", 
        }
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_users_service(body):
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_user_by_id_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_user_by_email_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def read_user_by_name_service(body):
    if not body:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }
        



def update_user_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }


def delete_user_service(body):
    if body is None:
        return ResponseConstant.NO_SUCH_ISSUER
    return {
        "responseCode": ResponseConstant.SUCCESS.responseCode,
        "responseMessage": ResponseConstant.SUCCESS.responseMessage, 
        "body" : body
        }



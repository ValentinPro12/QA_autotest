class BodyBuild:
    @staticmethod
    def user_body_create(username: str, password: str, email: str, user_info_loader_type_id: int):
        request_body = {"Signup": {"username": username, "password": password,
                                   "email": email,
                                   "user_info_loader_type_id": user_info_loader_type_id}}
        return request_body

    @staticmethod
    def user_body(roleName: str, user_id: int):
        request_body = {"roleName": roleName, "userId": user_id}
        return request_body

    @staticmethod
    def scale(scalesId: int, user_id: int):
        request_body = {"userId": user_id, "scalesId": type(scalesId)}
        return request_body

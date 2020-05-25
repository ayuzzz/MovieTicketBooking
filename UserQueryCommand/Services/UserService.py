from Repository.UserRepository import UserRepository


class UserService:
    userRepository = UserRepository()

    def getUserDetails(self, userid):
        return self.userRepository.getUserDetails(userid)

    def submitUserDetails(self, jsonRequest):
        return self.userRepository.submitUserDetails(jsonRequest)

    def validateUsernamePassword(self, username_password):
        return self.userRepository.validateUsernamePassword(username_password)
import json


class RestApiTool:

    def __init__(self):
        self.__subject: str = str()
        self.__description: str = str()
        self.__requester_id: int = int()
        self.__requester_name: str = str()
        self.__impact_details: str = str()

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value: str):
        self.__subject = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    @property
    def requester_id(self):
        return self.__requester_id

    @requester_id.setter
    def requester_id(self, value: int):
        self.__requester_id = value

    @property
    def requester_name(self):
        return self.__requester_name

    @requester_name.setter
    def requester_name(self, value: str):
        self.__requester_name = value

    @property
    def impact_details(self):
        return self.__impact_details

    @impact_details.setter
    def impact_details(self, value: str):
        self.__impact_details = value

    def createRequest(self):
        request = dict()
        request["subject"] = self.__subject
        request["description"] = self.__description
        requester = {"id": self.__requester_id, "name": self.__requester_name}
        request["requester"] = requester
        request["impact_details"] = self.__impact_details
        api_response = {"request": request}
        data = {'input_data': api_response}
        json_object = json.dumps(data, indent=4)
        return json_object

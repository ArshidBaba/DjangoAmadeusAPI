from amadeus import Client, ResponseError, Location
from django.http import JsonResponse

amadeus = Client(
    client_id = "aRUhXmiqALwk9IT5nZeGk6Ciw49cMkPd",
    client_secret = "ko7wEPGTeAcoABge"
)


def select_destination(req, param):
    if req.method == "GET":
        try:
            print(param)
            response = amadeus.reference_data.locations.get(
                keyword=param, subType=Location.ANY
            )
            context = {
                "data": response.data
            }
            return JsonResponse(context)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})


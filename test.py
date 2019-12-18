browse_quotes_response = {
  "Quotes": [
    {
      "QuoteId": 1,
      "MinPrice": 381,
      "Direct": True,
      "OutboundLeg": {
        "CarrierIds": [
          470
        ],
        "OriginId": 68033,
        "DestinationId": 42833,
        "DepartureDate": "2017-02-03T00:00:00"
      },
      "InboundLeg": {
        "CarrierIds": [
          470
        ],
        "OriginId": 42833,
        "DestinationId": 68033,
        "DepartureDate": "2017-02-06T00:00:00"
      },
      "QuoteDateTime": "2016-11-09T21:20:00"
    },
  ...
  ],
  "Places": [
    {
      "PlaceId": 837,
      "Name": "United Arab Emirates",
      "Type": "Country",
      "SkyscannerCode": "AE"
    },
  ...
  ],
  "Carriers": [
    {
      "CarrierId": 29,
      "Name": "Mombasa Air Safari"
    },
    {
      "CarrierId": 173,
      "Name": "Silver Airways"
    },
  ...
  ],
  "Currencies": [
    {
      "Code": "EUR",
      "Symbol": "€",
      "ThousandsSeparator": " ",
      "DecimalSeparator": ",",
      "SymbolOnLeft": False,
      "SpaceBetweenAmountAndSymbol": True,
      "RoundingCoefficient": 0,
      "DecimalDigits": 2
    }
  ]
}
browse_routes_response = {
  "Routes": [
    {
      "OriginId": 1811,
      "DestinationId": 1845,
      "QuoteIds": [
        1,
        2
      ],
      "Price": 326,
      "QuoteDateTime": "2016-11-13T01:30:00"
    },
    {
      "OriginId": 1811,
      "DestinationId": 929,
      "QuoteIds": [
        3
      ],
      "Price": 150,
      "QuoteDateTime": "2016-11-09T17:44:00"
    },
  ...
  ],
  "Quotes": [
    {
      "QuoteId": 1,
      "MinPrice": 381,
      "Direct": True,
      "OutboundLeg": {
        "CarrierIds": [
          470
        ],
        "OriginId": 68033,
        "DestinationId": 42833,
        "DepartureDate": "2017-02-03T00:00:00"
      },
      "InboundLeg": {
        "CarrierIds": [
          470
        ],
        "OriginId": 42833,
        "DestinationId": 68033,
        "DepartureDate": "2017-02-06T00:00:00"
      },
      "QuoteDateTime": "2016-11-09T21:20:00"
    },
  ...
  ],
  "Places": [
    {
      "PlaceId": 837,
      "Name": "United Arab Emirates",
      "Type": "Country",
      "SkyscannerCode": "AE"
    },
  ...
  ],
  "Carriers": [
    {
      "CarrierId": 29,
      "Name": "Mombasa Air Safari"
    },
    {
      "CarrierId": 173,
      "Name": "Silver Airways"
    },
  ...
  ],
  "Currencies": [
    {
      "Code": "EUR",
      "Symbol": "€",
      "ThousandsSeparator": " ",
      "DecimalSeparator": ",",
      "SymbolOnLeft": False,
      "SpaceBetweenAmountAndSymbol": False,
      "RoundingCoefficient": 0,
      "DecimalDigits": 2
    }
  ]
}
# browse_routes_response =
# browse_routes_response =
# browse_routes_response =


for index in browse_quotes_response:
    # print(index)
    pass

print(browse_quotes_response)
print(browse_quotes_response["Quotes"])


travel_origin = [
    "EWR",
    "ABE",
    "PHL"
]

travel_destination = [
    "YYC",
    "YYT",
    "YDF",
    "ANC"
]

departure_dates = [
    "2020-09-10",
    "2020-10-11"
]

return_dates = [
    "2020-09-12",
    "2020-10-13"
]
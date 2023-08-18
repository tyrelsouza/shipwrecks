pipeline = [
    {
        '$geoNear': {
            'near': {
                'type': 'Point', 
                'coordinates': [
                    -78.9, 35.9
                ]
            }, 
            'distanceField': 'distance', 
            'maxDistance': 160934.4,
            'spherical': True
        }
    }
]

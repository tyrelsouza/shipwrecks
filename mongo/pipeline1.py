pipeline = [
    {
        '$addFields': {
            'location': {
                'type': 'Point', 
                'coordinates': [
                    {
                        '$toDouble': '$latdec'
                    }, {
                        '$toDouble': '$londec'
                    }
                ]
            }
        }
    }, {
        '$match': {
            'location': {
                '$geoWithin': {
                    '$centerSphere': [
                        [
                            35.9, -78.9
                        ], 100 / 3963.2
                    ]
                }
            }
        }
    }, {
        '$project': {
            '_id': 1, 
            'recrd': 1, 
            'vesslterms': 1, 
            'feature_type': 1, 
            'chart': 1, 
            'latdec': 1, 
            'londec': 1, 
            'gp_quality': 1, 
            'depth': 1, 
            'sounding_type': 1, 
            'history': 1, 
            'quasou': 1, 
            'watlev': 1, 
            'coordinates': 1
        }
    }
]

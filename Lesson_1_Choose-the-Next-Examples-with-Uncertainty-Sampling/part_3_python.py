pool = [

    {"id": "img_101", "probs": [0.92, 0.05, 0.03]},

    {"id": "img_102", "probs": [0.40, 0.35, 0.25]},

    {"id": "img_103", "probs": [0.10, 0.20, 0.70]},

    {"id": "img_104", "probs": [0.51, 0.49, 0.00]},

    {"id": "img_105", "probs": [0.60, 0.05, 0.35]},

    ]



for item in pool:

    item["uncertainty"] = 1 - max(item["probs"])

    print(item["id"], round(item["uncertainty"], 2))
